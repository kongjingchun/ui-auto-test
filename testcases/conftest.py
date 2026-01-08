# encoding: utf-8
# @File  : conftest.py
# @Author: 孔敬淳
# @Date  : 2025/12/18/15:24
# @Desc  : pytest配置文件，用于定义测试用例的fixture和全局配置

import os
import shutil
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


def pytest_sessionstart(session):
    """pytest会话开始时执行，删除并重新创建UIreport目录"""
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
    test_name = item.function.__doc__ if item.function.__doc__ else item.name
    log.info("=" * 80)
    log.info(f"{'=' * 20} 开始执行测试用例: {test_name} {'=' * 20}")
    log.info("=" * 80)


def pytest_runtest_teardown(item, nextitem):
    """测试用例执行后调用，输出测试用例结束分界线"""
    test_name = item.function.__doc__ if item.function.__doc__ else item.name
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
    out = yield
    report = out.get_result()
    # 将测试函数的文档字符串添加到报告描述中
    report.description = str(item.function.__doc__)
    # 测试用例执行阶段
    if report.when == "call":
        test_name = item.function.__doc__ if item.function.__doc__ else item.name
        # 如果测试失败，添加失败截图到报告
        if report.failed:
            log.info("=" * 80)
            log.info(f"{'=' * 20} 测试用例执行失败: {test_name} {'=' * 20}")
            log.info("=" * 80)
            add_img_2_report(get_driver, "失败截图", need_sleep=False)
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
