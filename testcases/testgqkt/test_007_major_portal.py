# encoding: utf-8
# @File  : test_007_major_portal.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 专业门户管理测试用例

import allure
import pytest

from common.report_add_img import add_img_2_report
from testcases.helpers.test_context_helper import TestContextHelper
from common.yaml_config import GetConf
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

        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录并进入专业门户管理"):
            result = helper.setup_context(
                user_info=prof_cms_user_info,
                menu_name="专业门户管理"
            )
            assert result is True, "登录或导航失败"

        with allure.step("根据专业名称点击编辑页面按钮"):
            result = MajorPortalManagePage().click_edit_page_button_by_major_name(driver, major_info['专业名称'])
            add_img_2_report(driver, "根据专业名称点击编辑页面按钮")
            assert result is True, "根据专业名称点击编辑页面按钮失败"

        with allure.step("编辑门户"):
            result = MajorPortalManagePage().edit_portal(driver, major_info['专业名称'])
            add_img_2_report(driver, "编辑门户")
            assert result is True, "编辑门户失败"
