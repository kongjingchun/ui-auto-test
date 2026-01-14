# encoding: utf-8
# @File  : conftest.py
# @Author: 孔敬淳
# @Date  : 2025/12/18/15:24
# @Desc  : pytest配置文件，用于定义测试用例的fixture和全局配置

import os
import shutil
from datetime import datetime

import pytest

from common.ding_talk import send_ding_talk
from common.process_file import Process  # 使用文件存储测试进度
from common.report_add_img import add_img_2_report
from common.tools import get_project_path
from common.yaml_config import GetConf
from config.driver_config import DriverConfig
from logs.log import log

# 配置Allure测试报告默认语言为中文
os.environ.setdefault('ALLURE_LANG', 'zh-CN')

# 全局变量：收集测试用例执行结果
_test_results = {
    'passed': [],
    'failed': [],
    'skipped': [],
    'start_time': None,
    'end_time': None
}


def pytest_sessionstart(session):
    """pytest会话开始时执行，删除并重新创建UIreport目录"""
    global _test_results
    # 初始化测试结果收集
    _test_results = {
        'passed': [],
        'failed': [],
        'skipped': [],
        'start_time': datetime.now(),
        'end_time': None
    }
    
    uireport_path = os.path.join(get_project_path(), "UIreport")
    if os.path.exists(uireport_path):
        try:
            shutil.rmtree(uireport_path)
            log.info(f"已删除UIreport目录: {uireport_path}")
        except Exception as e:
            log.warning(f"删除UIreport目录失败: {e}")
    else:
        log.info(f"UIreport目录不存在，无需删除: {uireport_path}")

    # 重新创建UIreport目录，确保后续测试可以正常写入报告
    try:
        os.makedirs(uireport_path, exist_ok=True)
        log.info(f"已创建UIreport目录: {uireport_path}")
    except Exception as e:
        log.warning(f"创建UIreport目录失败: {e}")


def pytest_configure(config):
    """注册自定义marker"""
    config.addinivalue_line(
        "markers", "skip_local: 标记在本地部署环境下需要跳过的测试用例"
    )
    config.addinivalue_line(
        "markers", "skip_remote: 标记在网络部署环境下需要跳过的测试用例"
    )


def pytest_collection_modifyitems(config, items):
    """在收集测试用例时，根据部署环境自动跳过标记的用例"""
    is_local = GetConf().is_local_deploy()

    for item in items:
        # 如果标记了 skip_local 且是本地部署，则跳过
        if item.get_closest_marker("skip_local") and is_local:
            item.add_marker(pytest.mark.skip(reason="本地部署环境，跳过该测试用例"))
        # 如果标记了 skip_remote 且是网络部署，则跳过
        elif item.get_closest_marker("skip_internet") and not is_local:
            item.add_marker(pytest.mark.skip(reason="网络部署环境，跳过该测试用例"))


def pytest_collection_finish(session):
    """pytest收集完测试用例后执行，初始化测试进度"""
    total = len(session.items)
    Process().reset_all()  # 清空之前的进度数据
    Process().init_process(total)  # 初始化新的测试进度


def pytest_runtest_setup(item):
    """测试用例执行前调用，输出测试用例开始分界线"""
    # 只获取文档字符串的第一行（简短描述），去掉 Args 和 Returns 部分
    if item.function.__doc__:
        test_name = item.function.__doc__.strip().split('\n')[0]
    else:
        test_name = item.name
    log.info("=" * 80)
    log.info(f"{'=' * 20} 开始执行测试用例: {test_name} {'=' * 20}")
    log.info("=" * 80)


def pytest_runtest_teardown(item, nextitem):
    """测试用例执行后调用，输出测试用例结束分界线"""
    # 只获取文档字符串的第一行（简短描述），去掉 Args 和 Returns 部分
    if item.function.__doc__:
        test_name = item.function.__doc__.strip().split('\n')[0]
    else:
        test_name = item.name
    # 获取测试结果（通过检查是否有异常）
    result_status = "执行完成"
    log.info("=" * 80)
    log.info(f"{'=' * 20} 测试用例{result_status}: {test_name} {'=' * 20}")
    log.info("=" * 80)


@pytest.fixture()
def driver():
    """
    WebDriver fixture，用于自动化测试的浏览器驱动管理

    该fixture会在测试用例执行前创建WebDriver实例，
    在测试用例执行后自动关闭浏览器，确保资源正确释放。

    使用方式:
        在测试函数中添加driver参数即可自动注入WebDriver实例

        def test_example(driver):
            driver.get("https://example.com")
            # 执行测试操作...

    Yields:
        WebDriver: 配置好的浏览器驱动实例
    """
    global get_driver
    # 通过DriverConfig获取配置好的WebDriver实例
    get_driver = DriverConfig.driver_config()

    # yield将driver实例传递给测试用例
    yield get_driver

    # 测试用例执行完毕后，关闭浏览器并释放资源
    get_driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """pytest钩子函数，生成测试报告并在失败时自动截图"""
    global _test_results
    out = yield
    report = out.get_result()
    # 将测试函数的文档字符串添加到报告描述中
    report.description = str(item.function.__doc__)
    
    # 只获取文档字符串的第一行（简短描述），去掉 Args 和 Returns 部分
    if item.function.__doc__:
        test_name = item.function.__doc__.strip().split('\n')[0]
    else:
        test_name = item.name
    
    # 记录测试用例信息
    test_info = {
        'name': test_name,
        'nodeid': item.nodeid,
        'duration': getattr(report, 'duration', 0),
        'outcome': report.outcome,
        'when': report.when
    }
    
    # 处理跳过的用例（可能在 setup 阶段就跳过）
    if report.skipped:
        # 避免重复记录跳过的用例
        if not any(t['nodeid'] == item.nodeid for t in _test_results['skipped']):
            _test_results['skipped'].append(test_info)
        return
    
    # 处理 setup 阶段的错误（ERROR）
    if report.when == "setup" and report.failed:
        # 避免重复记录错误的用例
        if not any(t['nodeid'] == item.nodeid for t in _test_results['failed']):
            _test_results['failed'].append(test_info)
            Process().update_fail()
            Process().insert_into_fail_testcase_names(report.description)
        return
    
    # 测试用例执行阶段（call）
    if report.when == "call":
        # 如果测试失败，添加失败截图到报告
        if report.failed:
            log.info("=" * 80)
            log.info(f"{'=' * 20} 测试用例执行失败: {test_name} {'=' * 20}")
            log.info("=" * 80)
            try:
                add_img_2_report(get_driver, "失败截图", need_sleep=False)
            except:
                pass  # 如果 driver 未初始化，跳过截图
            Process().update_fail()  # 失败用例计数+1
            Process().insert_into_fail_testcase_names(report.description)  # 记录失败用例名称
            # 避免重复记录
            if not any(t['nodeid'] == item.nodeid for t in _test_results['failed']):
                _test_results['failed'].append(test_info)
        elif report.passed:
            log.info("=" * 80)
            log.info(f"{'=' * 20} 测试用例执行成功: {test_name} {'=' * 20}")
            log.info("=" * 80)
            # 成功用例计数+1
            Process().update_success()
            # 记录成功用例名称
            Process().insert_into_success_testcase_names(report.description)
            _test_results['passed'].append(test_info)
        
        # 本地部署时不发送钉钉消息
        if not GetConf().is_local_deploy():
            process = Process().get_process()  # 获取测试进度
            webhook = GetConf().get_dingding_webhook()
            send_ding_talk(
                webhook,
                "测试用例:"
                + report.description
                + "\n测试结果: "
                + report.outcome
                + "\n自动化测试进度: "
                + process,
            )


def pytest_sessionfinish(session, exitstatus):
    """pytest会话结束时执行，输出测试结果汇总"""
    global _test_results
    _test_results['end_time'] = datetime.now()
    
    # 计算总执行时间
    if _test_results['start_time'] and _test_results['end_time']:
        duration = _test_results['end_time'] - _test_results['start_time']
        total_seconds = duration.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        if hours > 0:
            duration_str = f"{hours}小时{minutes}分钟{seconds}秒"
        elif minutes > 0:
            duration_str = f"{minutes}分钟{seconds}秒"
        else:
            duration_str = f"{seconds}秒"
    else:
        duration_str = "未知"
    
    # 统计信息
    total = len(_test_results['passed']) + len(_test_results['failed']) + len(_test_results['skipped'])
    passed_count = len(_test_results['passed'])
    failed_count = len(_test_results['failed'])
    skipped_count = len(_test_results['skipped'])
    # 实际执行的用例数（不包含跳过的）
    executed_count = passed_count + failed_count
    
    # 输出漂亮的汇总报告
    log.info("")
    log.info("")
    log.info("╔" + "═" * 98 + "╗")
    log.info("║" + " " * 30 + "📊 测试执行结果汇总报告" + " " * 44 + "║")
    log.info("╠" + "═" * 98 + "╣")
    log.info("║" + " " * 98 + "║")
    
    # 执行时间信息
    start_time_str = _test_results['start_time'].strftime('%Y-%m-%d %H:%M:%S') if _test_results['start_time'] else '未知'
    end_time_str = _test_results['end_time'].strftime('%Y-%m-%d %H:%M:%S') if _test_results['end_time'] else '未知'
    log.info(f"║  执行时间: {start_time_str} - {end_time_str}" + " " * (98 - 20 - len(start_time_str) - len(end_time_str) - 3) + "║")
    log.info(f"║  总执行时长: {duration_str}" + " " * (98 - 12 - len(duration_str)) + "║")
    log.info("║" + " " * 98 + "║")
    
    # 执行统计
    log.info("╠" + "─" * 98 + "╣")
    log.info("║" + " " * 35 + "📈 执行统计" + " " * 52 + "║")
    log.info("╠" + "─" * 98 + "╣")
    log.info(f"║  总用例数: {total}" + " " * (98 - 11 - len(str(total))) + "║")
    
    if executed_count > 0:
        # 成功和失败的百分比基于实际执行的用例数（不包含跳过的）
        passed_pct = passed_count / executed_count * 100
        failed_pct = failed_count / executed_count * 100
        log.info(f"║  ✅ 成功用例: {passed_count:3d} ({passed_pct:5.1f}%)" + " " * (98 - 20 - len(str(passed_count)) - len(f"{passed_pct:.1f}")) + "║")
        log.info(f"║  ❌ 失败用例: {failed_count:3d} ({failed_pct:5.1f}%)" + " " * (98 - 20 - len(str(failed_count)) - len(f"{failed_pct:.1f}")) + "║")
    else:
        log.info("║  ✅ 成功用例:   0" + " " * 82 + "║")
        log.info("║  ❌ 失败用例:   0" + " " * 82 + "║")
    
    # 跳过用例不显示百分比
    log.info(f"║  ⏭️  跳过用例: {skipped_count:3d}" + " " * (98 - 13 - len(str(skipped_count))) + "║")
    
    log.info("║" + " " * 98 + "║")
    
    # 成功用例列表
    if _test_results['passed']:
        log.info("╠" + "─" * 98 + "╣")
        log.info("║" + " " * 35 + "✅ 成功用例列表" + " " * 48 + "║")
        log.info("╠" + "─" * 98 + "╣")
        for idx, test in enumerate(_test_results['passed'], 1):
            duration_s = test['duration'] if test['duration'] > 0 else 0
            test_name = test['name']
            # 确保名称不超过一定长度
            if len(test_name) > 70:
                test_name = test_name[:67] + "..."
            if duration_s > 0:
                log.info(f"║  {idx:2d}. {test_name}" + " " * (98 - 6 - len(str(idx)) - len(test_name)) + "║")
                log.info(f"║      执行时长: {duration_s:.2f}s" + " " * (98 - 15 - len(f"{duration_s:.2f}")) + "║")
            else:
                log.info(f"║  {idx:2d}. {test_name}" + " " * (98 - 6 - len(str(idx)) - len(test_name)) + "║")
        log.info("║" + " " * 98 + "║")
    
    # 失败用例列表
    if _test_results['failed']:
        log.info("╠" + "─" * 98 + "╣")
        log.info("║" + " " * 35 + "❌ 失败用例列表" + " " * 48 + "║")
        log.info("╠" + "─" * 98 + "╣")
        for idx, test in enumerate(_test_results['failed'], 1):
            duration_s = test['duration'] if test['duration'] > 0 else 0
            test_name = test['name']
            # 确保名称不超过一定长度
            if len(test_name) > 70:
                test_name = test_name[:67] + "..."
            log.info(f"║  {idx:2d}. {test_name}" + " " * (98 - 6 - len(str(idx)) - len(test_name)) + "║")
            if duration_s > 0:
                log.info(f"║      执行时长: {duration_s:.2f}s" + " " * (98 - 15 - len(f"{duration_s:.2f}")) + "║")
            if test.get('when') == 'setup':
                log.info("║      错误类型: 初始化阶段错误" + " " * 66 + "║")
            # 显示用例路径（截断过长的路径）
            nodeid = test['nodeid']
            if len(nodeid) > 85:
                nodeid = "..." + nodeid[-82:]
            log.info(f"║      用例路径: {nodeid}" + " " * (98 - 14 - len(nodeid)) + "║")
        log.info("║" + " " * 98 + "║")
    
    # 跳过用例列表
    if _test_results['skipped']:
        log.info("╠" + "─" * 98 + "╣")
        log.info("║" + " " * 35 + "⏭️  跳过用例列表" + " " * 48 + "║")
        log.info("╠" + "─" * 98 + "╣")
        for idx, test in enumerate(_test_results['skipped'], 1):
            test_name = test['name']
            # 确保名称不超过一定长度
            if len(test_name) > 70:
                test_name = test_name[:67] + "..."
            log.info(f"║  {idx:2d}. {test_name}" + " " * (98 - 6 - len(str(idx)) - len(test_name)) + "║")
        log.info("║" + " " * 98 + "║")
    
    # 总结
    log.info("╠" + "═" * 98 + "╣")
    if failed_count == 0 and total > 0:
        log.info("║" + " " * 35 + "🎉 所有测试用例执行成功！" + " " * 40 + "║")
    elif failed_count > 0:
        log.info(f"║" + " " * 30 + f"⚠️  有 {failed_count} 个测试用例执行失败，请检查！" + " " * (98 - 40 - len(str(failed_count))) + "║")
    else:
        log.info("║" + " " * 40 + "未执行任何测试用例" + " " * 48 + "║")
    log.info("╚" + "═" * 98 + "╝")
    log.info("")
    log.info("")
