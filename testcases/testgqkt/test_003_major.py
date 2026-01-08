# encoding: utf-8
# @File  : test_003_major.py
# @Author: 孔敬淳
# @Date  : 2025/12/30/16:21
# @Desc  :
import allure
import pytest

from common.report_add_img import add_img_2_report
from testcases.helpers.test_context_helper import TestContextHelper
from common.yaml_config import GetConf
from page.ai_major.MajorManagePage import MajorManagePage


class TestMajor:
    """创建专业测试"""

    @pytest.mark.run(order=130)
    @allure.story("创建专业")
    def test_001_create_major(self, driver):
        """创建专业流程"""
        # 教务管理员账号
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # 新建的专业信息
        major_info = GetConf().get_info("major")

        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录并进入专业管理"):
            result = helper.setup_context(
                user_info=dean_cms_user_info,
                menu_name="专业管理"
            )
            assert result is True, "登录或导航失败"

        with allure.step("创建专业"):
            result = MajorManagePage().create_major(driver, major_info)
            add_img_2_report(driver, "创建专业")
            assert result is True, "创建专业失败"
