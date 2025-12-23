# encoding: utf-8
# @File  : test_login.py
# @Author: kongjingchun
# @Date  : 2025/12/01/18:37
# @Desc  :
from time import sleep

import allure
import pytest

from common.report_add_img import add_img_2_report
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage


class TestLogin:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录")
    def test_login(self, driver):
        with allure.step("登录"):
            LoginPage().login(driver, "kjc", True)
            sleep(3)
            add_img_2_report(driver, "登录")
