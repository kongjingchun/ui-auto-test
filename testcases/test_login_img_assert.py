# encoding: utf-8
# @File  : test_login_img_assert.py
# @Author: kongjingchun
# @Date  : 2025/12/18/21:47
# @Desc  :
from time import sleep

import allure
import pytest

from common.report_add_img import add_img_2_report
from page.LoginPage import LoginPage


class TestLoginAssert:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录后断言图片")
    def test_login_assert(self, driver):
        """登录后断言图片"""
        with allure.step("登录"):
            LoginPage().login(driver, "william")
            add_img_2_report(driver, "登录")

        with allure.step("断言图片"):
            assert LoginPage().login_assert(driver, "123.png") > 0.9
