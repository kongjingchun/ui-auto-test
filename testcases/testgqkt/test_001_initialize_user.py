# encoding: utf-8
# @File  : test_001_initialize_user.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/21:27
# @Desc  :

import allure

from common.report_add_img import add_img_2_report
from common.yaml_config import GetConf
from logs.log import log
from page.LeftMenuPage import LeftMenuPage
from page.login.LoginPage import LoginPage
from page.TopMenuPage import TopMenuPage
from page.dean_manage.UserManagePage import UserManagePage
from page.cms.CmsUserManagePage import CmsUserManage


class TestInitializeUser:

    @allure.story("初始化账号")
    def test_001_initialize_user(self, driver):
        """
        测试初始化教务账号流程
        :param driver: WebDriver实例
        :return: None
        """
        # 学校名称
        school_name = GetConf().get_school_name()
        # 超级管理员信息（账密）
        superadmin = GetConf().get_user_info("superadmin")
        # 创建的CMS教务管理员信息
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # 创建的教务管理员信息
        dean_user_info = GetConf().get_user_info("dean")
        # 创建的CMS专业负责人信息
        prof_cms_user_info = GetConf().get_user_info("prof_cms")
        # 创建的专业负责人信息
        prof_user_info = GetConf().get_user_info("prof")

        with allure.step("api注册cms账户"):
            result = CmsUserManage().register_cms_user(dean_cms_user_info)
            assert result is True, "api注册教务账户失败"
            result = CmsUserManage().register_cms_user(prof_cms_user_info)
            assert result is True, "api注册专业负责人账户失败"

        with allure.step("登录"):
            result = LoginPage().user_login(driver, superadmin)
            add_img_2_report(driver, "登录")
            assert result is True, "登录失败"

        with allure.step("切换到cms"):
            result = TopMenuPage().switch_school(driver, "CMS管理系统")
            add_img_2_report(driver, "切换到cms")
            assert result is True, "切换到CMS管理系统失败"

        with allure.step("点击到全部用户管理"):
            result = LeftMenuPage().click_two_level_menu(driver, "全部用户管理")
            add_img_2_report(driver, "点击到全部用户管理")
            assert result is True, "点击到全部用户管理失败"

        with allure.step("查询cms用户ID"):
            dean_user_id = CmsUserManage().search_cms_user(driver, dean_cms_user_info["username"])
            add_img_2_report(driver, "查询教务管理员ID")
            assert dean_user_id is not None and dean_user_id != "", "查询教务管理员ID失败，未找到用户"
            log.info("教务管理员id为:" + dean_user_id)
            prof_user_id = CmsUserManage().search_cms_user(driver, prof_cms_user_info["username"])
            add_img_2_report(driver, "查询专业负责人ID")
            assert prof_user_id is not None and prof_user_id != "", "查询专业负责人ID失败，未找到用户"
            log.info("专业负责人id为:" + prof_user_id)

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

        with allure.step("创建用户"):
            result = UserManagePage().create_user(driver, role_name="创建教务管理员", user_info=dean_user_info)
            add_img_2_report(driver, "创建教务管理员")
            assert result is True, "创建教务管理员失败"
            result = UserManagePage().create_user(driver, role_name="创建专业负责人", user_info=prof_user_info)
            add_img_2_report(driver, "创建专业负责人")
            assert result is True, "创建专业负责人失败"

        with allure.step("用户绑定"):
            result = UserManagePage().bind_user(driver, dean_user_info["工号"], dean_user_id)
            add_img_2_report(driver, "教务管理员绑定")
            assert result is True, "教务管理员绑定失败"
            result = UserManagePage().bind_user(driver, prof_user_info["工号"], prof_user_id)
            add_img_2_report(driver, "专业负责人绑定")
            assert result is True, "专业负责人绑定失败"
