# encoding: utf-8
# @File  : conftest.py
# @Author: 孔敬淳
# @Date  : 2025/12/18/15:24
# @Desc  : pytest配置文件，用于定义测试用例的fixture和全局配置

import os
import pytest
from openpyxl.styles.builtins import total

from common.process_redis import Process
from common.report_add_img import add_img_2_report
from config.driver_config import DriverConfig

# 配置Allure测试报告默认语言为中文
os.environ.setdefault('ALLURE_LANG', 'zh-CN')


def pytest_collection_finish(session):
    """pytest收集完测试用例后执行，初始化测试进度"""
    total = len(session.items)
    Process().reset_all()  # 清空之前的进度数据
    Process().init_process(total)  # 初始化新的测试进度


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
            Process().update_fail()  # 失败用例计数+1
            Process().insert_into_fail_testcase_names(report.description)  # 记录失败用例名称
        elif report.passed:
            # 成功用例计数+1
            Process().update_success()
        else:
            pass
        process = Process().get_process()
        print(f"测试进度: {process}")
