# encoding: utf-8
# @File  : test_login_img_assert.py
# @Author: kongjingchun
# @Date  : 2025/12/18/21:47
# @Desc  :
import allure

from common.report_add_img import add_img_2_report
from page.LoginPage import LoginPage


class TestLoginAssert:
    @allure.feature("登录")
    @allure.description("登录后判断图片是否存在")
    def test_login_img_assert(self, driver):
        with allure.step("登录"):
            LoginPage().login(driver, "jay")
            add_img_2_report(driver, "登录")
        with allure.step("判断图片是否存在"):
            LoginPage().login_assert(driver, "123.png")