# encoding: utf-8
# @File  : conftest.py
# @Author: 孔敬淳
# @Date  : 2025/12/18/15:24
# @Desc  : pytest配置文件，用于定义测试用例的fixture和全局配置

import os
import shutil
import pytest
import datetime

from common.ding_talk import send_ding_talk
from common.process_file import Process  # 使用文件存储测试进度
from common.report_add_img import add_img_2_report
from common.tools import get_project_path
from common.yaml_config import GetConf
from config.driver_config import DriverConfig
from logs.log import log

# 配置Allure测试报告默认语言为中文
os.environ.setdefault('ALLURE_LANG', 'zh-CN')


def pytest_sessionstart(session):
    """pytest会话开始时执行，删除并重新创建UIreport目录"""
    # 检查是否是真正的测试执行，而不是IDE的代码检查
    # 通过检查命令行参数或环境变量来判断
    # 如果只是代码检查（如pytest --collect-only），则不执行目录操作
    try:
        # 检查是否有--collect-only参数（只收集不执行）
        if hasattr(session.config, 'option') and hasattr(session.config.option, 'collectonly'):
            if session.config.option.collectonly:
                return
    except Exception:
        pass

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
    """pytest配置阶段执行（只调用一次），初始化测试环境"""
    # 注册自定义marker
    config.addinivalue_line(
        "markers", "skip_local: 标记在本地部署环境下需要跳过的测试用例"
    )
    config.addinivalue_line(
        "markers", "skip_remote: 标记在网络部署环境下需要跳过的测试用例"
    )


def pytest_collection_modifyitems(config, items):
    """在收集测试用例时，根据部署环境自动跳过标记的用例，并按照order标记全局排序"""
    is_local = GetConf().is_local_deploy()

    for item in items:
        # 如果标记了 skip_local 且是本地部署，则跳过
        if item.get_closest_marker("skip_local") and is_local:
            item.add_marker(pytest.mark.skip(reason="本地部署环境，跳过该测试用例"))
        # 如果标记了 skip_internet 且是网络部署，则跳过
        elif item.get_closest_marker("skip_internet") and not is_local:
            item.add_marker(pytest.mark.skip(reason="网络部署环境，跳过该测试用例"))

    # 按照order标记全局排序（pytest-ordering只在文件内排序，这里实现跨文件全局排序）
    def get_order(item):
        """获取测试用例的order值，如果没有order标记则返回999999（排在最后）"""
        run_marker = item.get_closest_marker("run")
        if run_marker and "order" in run_marker.kwargs:
            return run_marker.kwargs["order"]
        return 999999

    # 按照order值排序
    items.sort(key=get_order)


def pytest_collection_finish(session):
    """pytest收集完测试用例后执行，初始化测试进度（只在主进程中执行）"""
    # 检查是否是真正的测试执行（有测试用例要执行），而不是IDE的代码检查
    if not hasattr(session, 'items') or len(session.items) == 0:
        return

    # 只在主进程中初始化进度，避免并行执行时多个worker重复初始化
    if not hasattr(session.config, 'workerinput'):  # workerinput存在说明是worker进程
        total = len(session.items)
        Process().reset_all()  # 清空之前的进度数据
        Process().init_process(total)  # 初始化新的测试进度


def pytest_sessionfinish(session, exitstatus):
    """pytest会话结束时执行，生成测试执行结果汇总报告（只在主进程中执行）"""
    # 只在主进程中生成汇总报告，避免并行执行时多个worker重复输出
    if hasattr(session.config, 'workerinput'):  # workerinput存在说明是worker进程
        return

    # 检查是否是真正的测试执行，而不是IDE的代码检查
    # 参考pytest_sessionstart的检查方式
    try:
        # 检查是否有--collect-only参数（只收集不执行）
        if hasattr(session.config, 'option') and hasattr(session.config.option, 'collectonly'):
            if session.config.option.collectonly:
                return
    except Exception:
        pass

    # 获取测试结果统计
    total, success, fail, start_time = Process().get_result()

    # 记录结束时间（如果还没有记录）
    process_instance = Process()
    process_instance.write_end_time()

    # 获取结束时间并计算执行耗时
    process_data = process_instance._read_json_file(process_instance.process_file)
    end_time_str = process_data.get("end_time", "")

    # 计算执行耗时（精确到秒）
    duration_seconds = 0
    duration_str = "未知"
    try:
        if start_time and start_time != "-" and end_time_str:
            # 解析时间字符串（格式：2026-01-14 22:44:00.123456 或 2026-01-14 22:44:00）
            time_formats = [
                "%Y-%m-%d %H:%M:%S.%f",
                "%Y-%m-%d %H:%M:%S",
            ]
            start_dt = None
            end_dt = None

            for fmt in time_formats:
                try:
                    start_dt = datetime.datetime.strptime(str(start_time), fmt)
                    break
                except ValueError:
                    continue

            for fmt in time_formats:
                try:
                    end_dt = datetime.datetime.strptime(str(end_time_str), fmt)
                    break
                except ValueError:
                    continue

            if start_dt and end_dt:
                duration = end_dt - start_dt
                duration_seconds = int(duration.total_seconds())
                # 格式化显示：XX小时XX分XX秒 或 XX分XX秒 或 XX秒
                hours = duration_seconds // 3600
                minutes = (duration_seconds % 3600) // 60
                seconds = duration_seconds % 60

                if hours > 0:
                    duration_str = f"{hours}小时{minutes}分{seconds}秒"
                elif minutes > 0:
                    duration_str = f"{minutes}分{seconds}秒"
                else:
                    duration_str = f"{seconds}秒"
    except Exception as e:
        log.warning(f"计算执行耗时失败: {e}")
        duration_str = "计算失败"

    # 从pytest session的stats中获取跳过的用例数和名称
    skipped = 0
    skipped_testcase_names = []
    skipped_nodeids = set()  # 用于去重

    try:
        # 方法1: 从reporter stats中获取跳过的用例
        if hasattr(session.config, 'pluginmanager'):
            reporter = session.config.pluginmanager.get_plugin('terminalreporter')
            if reporter and hasattr(reporter, 'stats'):
                skipped_reports = reporter.stats.get('skipped', [])
                skipped = len(skipped_reports)
                # 提取跳过的用例nodeid
                for report in skipped_reports:
                    try:
                        if hasattr(report, 'nodeid'):
                            skipped_nodeids.add(report.nodeid)
                    except Exception:
                        pass
    except Exception:
        pass

    # 方法2: 从session.items中匹配跳过的用例并获取名称
    try:
        for item in session.items:
            # 检查测试项是否在跳过的列表中
            if item.nodeid in skipped_nodeids:
                # 获取用例名称（优先使用文档字符串）
                if item.function.__doc__:
                    test_name = item.function.__doc__.strip().split('\n')[0]
                else:
                    test_name = item.name
                skipped_testcase_names.append(test_name)
            # 或者检查是否有skip标记（作为备选方案）
            elif item.get_closest_marker('skip') or item.get_closest_marker('skipif'):
                if item.nodeid not in skipped_nodeids:
                    skipped_nodeids.add(item.nodeid)
                    if item.function.__doc__:
                        test_name = item.function.__doc__.strip().split('\n')[0]
                    else:
                        test_name = item.name
                    skipped_testcase_names.append(test_name)
    except Exception:
        pass

    # 如果还没有获取到跳过的数量，使用nodeids的数量
    if skipped == 0 and len(skipped_nodeids) > 0:
        skipped = len(skipped_nodeids)

    # 计算实际执行的用例数（成功数 + 失败数，这是最准确的方法）
    executed = success + fail

    # 重新计算跳过的用例数（总数 - 实际执行数，确保数据一致性）
    skipped = total - executed
    if skipped < 0:
        skipped = 0

    # 计算成功率和失败率（分母为实际执行的用例数）
    if executed > 0:
        success_rate = (success / executed) * 100
        fail_rate = (fail / executed) * 100
    else:
        success_rate = 0.0
        fail_rate = 0.0

    # 生成美观的汇总报告
    log.info("")
    log.info("=" * 80)
    log.info("=" * 80)
    log.info(" " * 20 + "📊 测试执行结果汇总报告 📊" + " " * 20)
    log.info("=" * 80)
    log.info("")

    # 总体统计
    log.info(" " * 25 + "【总体统计】" + " " * 25)
    log.info("-" * 80)
    log.info(f"  测试用例总数:     {total:>6} 个")
    log.info(f"  实际执行用例:     {executed:>6} 个")
    log.info(f"  跳过用例数:      {skipped:>6} 个")
    log.info(f"  执行耗时:        {duration_str:>15}")
    log.info("-" * 80)
    log.info("")

    # 执行结果统计
    log.info(" " * 25 + "【执行结果】" + " " * 25)
    log.info("-" * 80)
    log.info(f"  ✅ 执行成功:      {success:>6} 个  |  成功率: {success_rate:>6.2f}%")
    log.info(f"  ❌ 执行失败:      {fail:>6} 个  |  失败率: {fail_rate:>6.2f}%")
    log.info("-" * 80)
    log.info("")

    # 获取成功和失败的用例名称列表
    success_testcase_names = Process().get_success_testcase_names()
    fail_testcase_names = Process().get_fail_testcase_names()

    # 展示成功的用例名称（反转列表，因为存储时是插入到开头，所以顺序是倒的）
    if success_testcase_names:
        log.info(" " * 25 + "【执行成功的用例】" + " " * 25)
        log.info("-" * 80)
        # 反转列表，使顺序与执行顺序一致（从最早执行的到最晚执行的）
        success_testcase_names_reversed = list(reversed(success_testcase_names))
        for idx, testcase_name in enumerate(success_testcase_names_reversed, 1):
            # 只显示第一行（简短描述）
            display_name = testcase_name.strip().split('\n')[0] if testcase_name else "未知用例"
            log.info(f"  ✅ {idx:>3}. {display_name}")
        log.info("-" * 80)
        log.info("")
    else:
        if success > 0:
            log.info(" " * 25 + "【执行成功的用例】" + " " * 25)
            log.info("-" * 80)
            log.info("  ℹ️  成功用例名称未记录")
            log.info("-" * 80)
            log.info("")

    # 展示失败的用例名称（反转列表，因为存储时是插入到开头，所以顺序是倒的）
    if fail_testcase_names:
        log.info(" " * 25 + "【执行失败的用例】" + " " * 25)
        log.info("-" * 80)
        # 反转列表，使顺序与执行顺序一致（从最早执行的到最晚执行的）
        fail_testcase_names_reversed = list(reversed(fail_testcase_names))
        for idx, testcase_name in enumerate(fail_testcase_names_reversed, 1):
            # 只显示第一行（简短描述）
            display_name = testcase_name.strip().split('\n')[0] if testcase_name else "未知用例"
            log.info(f"  ❌ {idx:>3}. {display_name}")
        log.info("-" * 80)
        log.info("")
    else:
        if fail > 0:
            log.info(" " * 25 + "【执行失败的用例】" + " " * 25)
            log.info("-" * 80)
            log.info("  ℹ️  失败用例名称未记录")
            log.info("-" * 80)
            log.info("")

    # 展示跳过的用例名称
    if skipped_testcase_names:
        log.info(" " * 25 + "【跳过的用例】" + " " * 25)
        log.info("-" * 80)
        for idx, testcase_name in enumerate(skipped_testcase_names, 1):
            # 只显示第一行（简短描述）
            display_name = testcase_name.strip().split('\n')[0] if isinstance(testcase_name, str) else str(testcase_name)
            log.info(f"  ⏭️  {idx:>3}. {display_name}")
        log.info("-" * 80)
        log.info("")
    else:
        if skipped > 0:
            log.info(" " * 25 + "【跳过的用例】" + " " * 25)
            log.info("-" * 80)
            log.info("  ℹ️  跳过用例名称未记录")
            log.info("-" * 80)
            log.info("")

    # 最终状态
    log.info(" " * 25 + "【最终状态】" + " " * 25)
    log.info("-" * 80)
    if fail == 0 and executed > 0:
        log.info("  🎉 所有测试用例执行成功！")
    elif fail > 0:
        log.info(f"  ⚠️  有 {fail} 个测试用例执行失败，请检查失败详情")
    elif executed == 0:
        log.info("  ℹ️  没有实际执行的测试用例")
    log.info("-" * 80)
    log.info("")
    log.info("=" * 80)
    log.info("=" * 80)
    log.info("")


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


@pytest.fixture(scope="function")
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
    # 通过DriverConfig获取配置好的WebDriver实例
    driver_instance = DriverConfig.driver_config()

    # yield将driver实例传递给测试用例
    yield driver_instance

    # 测试用例执行完毕后，关闭浏览器并释放资源
    driver_instance.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """pytest钩子函数，生成测试报告并在失败时自动截图"""
    out = yield
    report = out.get_result()
    # 将测试函数的文档字符串添加到报告描述中
    report.description = str(item.function.__doc__)
    # 测试用例执行阶段
    if report.when == "call":
        # 只获取文档字符串的第一行（简短描述），去掉 Args 和 Returns 部分
        if item.function.__doc__:
            test_name = item.function.__doc__.strip().split('\n')[0]
        else:
            test_name = item.name
        # 如果测试失败，添加失败截图到报告
        if report.failed:
            log.info("=" * 80)
            log.info(f"{'=' * 20} 测试用例执行失败: {test_name} {'=' * 20}")
            log.info("=" * 80)
            # 尝试从item的fixture中获取driver实例
            try:
                driver_instance = item._request.getfixturevalue('driver') if hasattr(item, '_request') else None
                if driver_instance:
                    add_img_2_report(driver_instance, "失败截图", need_sleep=False)
            except (AttributeError, ValueError, KeyError):
                # 如果无法获取driver实例（可能已经被清理），记录警告但不中断流程
                log.warning("无法获取driver实例进行截图，可能已被清理")
            Process().update_fail()  # 失败用例计数+1
            Process().insert_into_fail_testcase_names(report.description)  # 记录失败用例名称
        elif report.passed:
            log.info("=" * 80)
            log.info(f"{'=' * 20} 测试用例执行成功: {test_name} {'=' * 20}")
            log.info("=" * 80)
            # 成功用例计数+1
            Process().update_success()
            # 记录成功用例名称
            Process().insert_into_success_testcase_names(report.description)
        else:
            pass
        # # 本地部署时不发送钉钉消息
        # if not GetConf().is_local_deploy():
        #     process = Process().get_process()  # 获取测试进度
        #     webhook = GetConf().get_dingding_webhook()
            # send_ding_talk(
            #     webhook,
            #     "测试用例:"
            #     + report.description
            #     + "\n测试结果: "
            #     + report.outcome
            #     + "\n自动化测试进度: "
            #     + process,
            # )
