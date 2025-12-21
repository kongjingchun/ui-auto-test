# encoding: utf-8
# @File  : conftest.py
# @Author: kongjingchun
# @Date  : 2025/12/18/15:24
# @Desc  : pytest配置文件，用于定义测试用例的fixture和全局配置

import pytest

from common.report_add_img import add_img_2_report
from config.driver_config import DriverConfig


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
        # 如果测试失败，添加失败截图到报告
        if report.failed:
            add_img_2_report(get_driver, "失败截图", need_sleep=False)
