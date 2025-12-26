# encoding: utf-8
# @File  : test_initialize_user.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/21:27
# @Desc  :
from time import sleep

import allure

from common.report_add_img import add_img_2_report
from common.yaml_config import GetConf
from logs.log import log
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.TopMenuPage import TopMenuPage
from page.academic_affairs.UserManagePage import UserManagePage
from page.cms.CmsUserManagePage import CmsUserManage


class TestInitializeUser:

    @allure.story("初始化教务账号")
    def test_001_initialize_user(self, driver):
        """
        测试gqkt
        :param driver:
        :return:
        """

        school_name = GetConf().get_school_name()
        with allure.step("登录"):
            LoginPage().user_login(driver, "superadmin")
            add_img_2_report(driver, "登录")
        with allure.step("切换学校"):
            TopMenuPage().switch_school(driver, school_name)
            add_img_2_report(driver, "切换学校")
        with allure.step("切换为机构管理员"):
            TopMenuPage().switch_role(driver, "机构管理员")
            add_img_2_report(driver, "切换为机构管理员")
        with allure.step("点击用户管理"):
            LeftMenuPage().click_two_level_menu(driver, "用户管理")
            add_img_2_report(driver, "点击用户管理")
        # with allure.step("创建教务管理员"):
        #     UserManagePage().create_user(driver, role_name="创建教务管理员", user="dean")
        # with allure.step("api注册教务管理员"):
        #     CmsUserManage().register_cms_user("dean_cms")
        with allure.step("切换到cms"):
            TopMenuPage().switch_school(driver, "CMS管理系统")
        with allure.step("点击到全部用户管理"):
            LeftMenuPage().click_two_level_menu(driver, "全部用户管理")
        with allure.step("搜索cms用户"):
            user_id = CmsUserManage().search_cms_user(driver, "dean_cms")
            log.info("查找到用户id:" + user_id)

