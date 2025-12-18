# encoding: utf-8
# @File  : test_login_img_assert.py
# @Author: kongjingchun
# @Date  : 2025/12/18/21:47
# @Desc  :
from page.LoginPage import LoginPage


class TestLoginAssert:
    def test_login_img_assert(self, driver):
        LoginPage().login(driver, "jay")
        LoginPage().login_assert(driver, '123.png')
