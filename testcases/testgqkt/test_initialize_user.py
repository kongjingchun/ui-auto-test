# encoding: utf-8
# @File  : test_initialize_user.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/21:27
# @Desc  :
from time import sleep

import allure

from common.report_add_img import add_img_2_report
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.TopMenuPage import TopMenuPage
from page.academic_affairs.UserManagePage import UserManagePage


class TestInitializeUser:

    @allure.story("初始化教务账号")
    def test_001_initialize_user(self, driver):
        """
        测试gqkt
        :param driver:
        :return:
        """
        with allure.step("登录"):
            LoginPage().user_login(driver, "superadmin")
            add_img_2_report(driver, "登录")
        with allure.step("切换学校"):
            TopMenuPage().switch_school(driver, "演示大学")
            add_img_2_report(driver, "切换学校")
        with allure.step("切换为机构管理员"):
            TopMenuPage().switch_role(driver, "机构管理员")
            add_img_2_report(driver, "切换为机构管理员")
        with allure.step("点击用户管理"):
            LeftMenuPage().click_two_level_menu(driver, "用户管理")
            add_img_2_report(driver, "点击用户管理")
        with allure.step("创建用户"):
            UserManagePage().create_user(driver, "创建教务管理员", "Auto教务", "AutoJiaoWu", "17601616126", "411861376@qq.com")
            sleep(3)
