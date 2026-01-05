# encoding: utf-8
# @File  : test_007_major_portal.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 专业门户管理测试用例

import allure
import pytest

from common.report_add_img import add_img_2_report
from common.yaml_config import GetConf
from page.LeftMenuPage import LeftMenuPage
from page.login.LoginPage import LoginPage
from page.ai_major.MajorPortalManagePage import MajorPortalManagePage


class TestMajorPortal:
    """专业门户管理测试"""

    @pytest.mark.run(order=180)
    @allure.story("专业门户管理")
    def test_001_major_portal_manage(self, driver):
        """专业门户管理流程"""
        # 专业管理员账号
        prof_cms_user_info = GetConf().get_user_info("prof_cms")
        # 专业信息
        major_info = GetConf().get_info("major")

        with allure.step("登录专业管理员"):
            result = LoginPage().user_login(driver, prof_cms_user_info)
            add_img_2_report(driver, "登录专业管理员")
            assert result is True, "登录专业管理员失败"

        with allure.step("点击左侧专业门户管理菜单"):
            result = LeftMenuPage().click_two_level_menu(driver, "专业门户管理")
            add_img_2_report(driver, "点击左侧专业门户管理菜单")
            assert result is True, "点击左侧专业门户管理菜单失败"

        with allure.step("根据专业名称点击编辑页面按钮"):
            result = MajorPortalManagePage().click_edit_page_button_by_major_name(driver, major_info['专业名称'])
            add_img_2_report(driver, "根据专业名称点击编辑页面按钮")
            assert result is True, "根据专业名称点击编辑页面按钮失败"

        with allure.step("编辑门户"):
            result = MajorPortalManagePage().edit_portal(driver, major_info['专业名称'])
            add_img_2_report(driver, "编辑门户")
            assert result is True, "编辑门户失败"
