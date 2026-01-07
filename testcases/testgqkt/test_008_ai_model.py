# encoding: utf-8
# @File  : test_008_ai_model.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 专业AI模型测试用例

import allure
import pytest

from common.report_add_img import add_img_2_report
from common.yaml_config import GetConf
from page.LeftMenuPage import LeftMenuPage
from page.login.LoginPage import LoginPage
from page.ai_major.MajorAIModel.MajorAIModelPage import MajorAIModelPage
from page.ai_major.MajorAIModel.MajorGraphModelPage import MajorGraphModelPage


class TestAIModel:
    """专业AI模型测试"""

    @pytest.mark.run(order=190)
    @allure.story("专业图谱概览")
    def test_001_major_graph_overview(self, driver):
        """专业图谱概览测试流程"""
        # 专业管理员账号
        prof_cms_user_info = GetConf().get_user_info("prof_cms")

        with allure.step("登录专业管理员"):
            result = LoginPage().user_login(driver, prof_cms_user_info)
            add_img_2_report(driver, "登录专业管理员")
            assert result is True, "登录专业管理员失败"

        with allure.step("点击左侧专业AI模型菜单"):
            result = LeftMenuPage().click_two_level_menu(driver, "专业AI模型")
            add_img_2_report(driver, "点击左侧专业AI模型菜单")
            assert result is True, "点击左侧专业AI模型菜单失败"
        with allure.step("创建专业图谱概览"):
            result = MajorGraphModelPage().create_major_graph_overview(driver)
            add_img_2_report(driver, "创建专业图谱概览")
            assert result is True, "创建专业图谱概览失败"
