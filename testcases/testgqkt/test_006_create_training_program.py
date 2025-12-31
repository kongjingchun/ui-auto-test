# encoding: utf-8
# @File  : test_006_create_training_program.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  :

import allure

from common.report_add_img import add_img_2_report
from common.yaml_config import GetConf
from page.LeftMenuPage import LeftMenuPage
from page.login.LoginPage import LoginPage
from page.ai_major.TrainingProgramManagePage import TrainingProgramManagePage


class TestCreateTrainingProgram:
    """创建培养方案测试"""

    @allure.story("创建培养方案")
    def test_001_create_training_program(self, driver):
        """创建培养方案流程"""
        # 专业管理员账号
        prof_cms_user_info = GetConf().get_user_info("prof_cms")
        # 新建的培养方案信息
        training_program_info = GetConf().get_info("training_program")

        with allure.step("登录专业管理员"):
            result = LoginPage().user_login(driver, prof_cms_user_info)
            add_img_2_report(driver, "登录专业管理员")
            assert result is True, "登录专业管理员失败"

        with allure.step("点击左侧培养方案管理菜单"):
            result = LeftMenuPage().click_two_level_menu(driver, "培养方案管理")
            add_img_2_report(driver, "点击左侧培养方案管理菜单")
            assert result is True, "点击左侧培养方案管理菜单失败"

        with allure.step("创建培养方案"):
            result = TrainingProgramManagePage().create_training_program(driver, training_program_info)
            add_img_2_report(driver, "创建培养方案")
            assert result is True, "创建培养方案失败"
