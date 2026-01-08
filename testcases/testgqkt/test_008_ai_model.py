# encoding: utf-8
# @File  : test_008_ai_model.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 专业AI模型测试用例

import allure
import pytest

from common.report_add_img import add_img_2_report
from testcases.helpers.test_context_helper import TestContextHelper
from common.yaml_config import GetConf
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

        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录并进入专业AI模型"):
            result = helper.setup_context(
                user_info=prof_cms_user_info,
                menu_name="专业AI模型"
            )
            assert result is True, "登录或导航失败"
        with allure.step("创建专业图谱概览"):
            result = MajorGraphModelPage().create_major_graph_overview(driver)
            add_img_2_report(driver, "创建专业图谱概览")
            assert result is True, "创建专业图谱概览失败"
