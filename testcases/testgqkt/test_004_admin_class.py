# encoding: utf-8
# @File  : test_004_admin_class.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  :

import allure
import pytest

from common.report_add_img import add_img_2_report
from common.yaml_config import GetConf
from page.LeftMenuPage import LeftMenuPage
from page.login.LoginPage import LoginPage
from page.dean_manage.AdminClassManagePage import AdminClassManagePage


class TestAdminClass:
    """创建行政班测试"""

    @pytest.mark.run(order=140)
    @allure.story("创建行政班")
    def test_001_create_admin_class(self, driver):
        """创建行政班流程"""
        # 教务管理员账号
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # 新建的行政班信息
        admin_class_info = GetConf().get_info("admin_class")

        with allure.step("登录教务管理员"):
            result = LoginPage().user_login(driver, dean_cms_user_info)
            add_img_2_report(driver, "登录教务管理员")
            assert result is True, "登录教务管理员失败"

        with allure.step("点击左侧行政班管理菜单"):
            result = LeftMenuPage().click_two_level_menu(driver, "行政班管理")
            add_img_2_report(driver, "点击左侧行政班管理菜单")
            assert result is True, "点击左侧行政班管理菜单失败"

        with allure.step("创建行政班"):
            result = AdminClassManagePage().create_admin_class(driver, admin_class_info)
            add_img_2_report(driver, "创建行政班")
            assert result is True, "创建行政班失败"
