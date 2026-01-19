# encoding: utf-8
# @File  : test_login.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/21:27
# @Desc  : 登录测试用例，符合Selenium官方Page Object Model和pytest框架规范

import allure
import pytest

from common.report_add_img import add_img_2_report
from page.login_page import LoginPage


class TestLogin:
    """登录测试类

    测试用例按照Selenium官方Page Object Model规范编写：
    1. 页面对象在测试用例中创建，driver通过pytest fixture注入
    2. 页面对象方法不包含driver参数
    3. 断言在测试用例中，不在页面对象中
    """

    @pytest.mark.run(order=1)
    @allure.story("账密登录")
    def test_01_login(self, driver):
        """
        测试账密登录流程

        Args:
            driver: WebDriver实例（通过pytest fixture注入）

        Returns:
            None
        """
        with allure.step("执行登录操作"):
            login_page = LoginPage(driver)
            result = login_page.login_first()
            add_img_2_report(driver, "登录操作")
            assert result is True, "登录操作失败"
