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
from page.dean_manage.UserManagePage import UserManagePage
from page.cms.CmsUserManagePage import CmsUserManage


class TestInitializeUser:

    @allure.story("初始化教务账号")
    def test_001_initialize_user(self, driver):
        """
        测试初始化教务账号流程
        :param driver: WebDriver实例
        :return: None
        """
        school_name = GetConf().get_school_name()
        
        with allure.step("登录"):
            result = LoginPage().user_login(driver, "superadmin")
            add_img_2_report(driver, "登录")
            assert result is True, "登录失败"
            
        with allure.step("切换学校"):
            result = TopMenuPage().switch_school(driver, school_name)
            add_img_2_report(driver, "切换学校")
            assert result is True, f"切换到{school_name}学校失败"
            
        with allure.step("切换为机构管理员"):
            result = TopMenuPage().switch_role(driver, "机构管理员")
            add_img_2_report(driver, "切换为机构管理员")
            assert result is True, "切换为机构管理员失败"
            
        with allure.step("点击用户管理"):
            result = LeftMenuPage().click_two_level_menu(driver, "用户管理")
            add_img_2_report(driver, "点击用户管理")
            assert result is True, "点击用户管理失败"
            
        with allure.step("创建教务管理员"):
            result = UserManagePage().create_user(driver, role_name="创建教务管理员", user="dean")
            add_img_2_report(driver, "创建教务管理员")
            assert result is True, "创建教务管理员失败"

        with allure.step("api注册教务管理员"):
            result = CmsUserManage().register_cms_user("dean_cms")
            assert result is True, "api注册教务管理员失败"
            
        with allure.step("切换到cms"):
            result = TopMenuPage().switch_school(driver, "CMS管理系统")
            add_img_2_report(driver, "切换到cms")
            assert result is True, "切换到CMS管理系统失败"
            
        with allure.step("点击到全部用户管理"):
            result = LeftMenuPage().click_two_level_menu(driver, "全部用户管理")
            add_img_2_report(driver, "点击到全部用户管理")
            assert result is True, "点击到全部用户管理失败"
            
        with allure.step("搜索cms用户"):
            user_id = CmsUserManage().search_cms_user(driver, "dean_cms")
            add_img_2_report(driver, "搜索cms用户")
            assert user_id is not None and user_id != "", "搜索cms用户失败，未找到用户"
            log.info("查找到用户id:" + user_id)
