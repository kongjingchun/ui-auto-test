# encoding: utf-8
# @File  : test_006_training_program.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  :

import allure
import pytest
from selenium.webdriver.common.by import By

from common.report_add_img import add_img_2_report
from common.yaml_config import GetConf
from page.LeftMenuPage import LeftMenuPage
from page.ai_major.TrainingProgramRevisionPage import TrainingProgramRevisionPage
from page.login.LoginPage import LoginPage
from page.ai_major.TrainingProgramManagePage import TrainingProgramManagePage


class TestTrainingProgram:
    """创建培养方案测试"""

    @pytest.mark.run(order=160)
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

    @pytest.mark.run(order=170)
    @allure.story("修订培养方案")
    def test_002_revision_training_program(self, driver):
        """修订培养方案流程"""
        # 专业管理员账号
        prof_cms_user_info = GetConf().get_user_info("prof_cms")
        # 新建的培养方案信息
        training_program_info = GetConf().get_info("training_program")
        # 课程信息
        course_info = GetConf().get_info("course")

        with allure.step("登录专业管理员"):
            result = LoginPage().user_login(driver, prof_cms_user_info)
            add_img_2_report(driver, "登录专业管理员")
            assert result is True, "登录专业管理员失败"

        with allure.step("点击左侧培养方案管理菜单"):
            result = LeftMenuPage().click_two_level_menu(driver, "培养方案管理")
            add_img_2_report(driver, "点击左侧培养方案管理菜单")
            assert result is True, "点击左侧培养方案管理菜单失败"

        with allure.step("根据方案名称点击修订按钮"):
            result = TrainingProgramManagePage().click_revision_button_by_program_name(driver, training_program_info['方案名称'])
            add_img_2_report(driver, "根据方案名称点击修订按钮")
            assert result is True, "根据方案名称点击修订按钮失败"

        with allure.step("更新专业信息"):
            result = TrainingProgramRevisionPage().update_major_info(driver, description="专业描述")
            add_img_2_report(driver, "更新专业信息")
            assert result is True, "更新专业信息失败"

        with allure.step("更新培养目标"):
            result1 = TrainingProgramRevisionPage().update_training_objective(driver, "培养目标概述1", "培养目标描述1")
            assert result1 is True, "更新培养目标1失败"
            result2 = TrainingProgramRevisionPage().update_training_objective(driver, "培养目标概述2", "培养目标描述2")
            assert result2 is True, "更新培养目标2失败"
            add_img_2_report(driver, "更新培养目标")

        with allure.step("更新毕业要求"):
            result1 = TrainingProgramRevisionPage().update_graduation_requirement(
                driver, description="毕业要求概述",
                indicator_index=1,
                indicator_name="指标点名称1",
                indicator_description="指标点描述1",
                decomposed_indicator_index=1,
                decomposed_indicator_name="分解指标点名称1.1",
                decomposed_indicator_description="分解指标点描述1.1")
            assert result1 is True, "更新毕业要求1失败"
            result2 = TrainingProgramRevisionPage().update_graduation_requirement(
                driver, description="毕业要求概述2",
                indicator_index=2,
                indicator_name="指标点名称2",
                indicator_description="指标点描述2",
                decomposed_indicator_index=1,
                decomposed_indicator_name="分解指标点名称2.1",
                decomposed_indicator_description="分解指标点描述2.1")
            assert result2 is True, "更新毕业要求2失败"
            add_img_2_report(driver, "更新毕业要求")

        with allure.step("更新目标支撑"):
            result1 = TrainingProgramRevisionPage().update_target_support(driver, index=1, level="高支撑")
            assert result1 is True, "更新目标支撑1失败"
            result2 = TrainingProgramRevisionPage().update_target_support(driver, index=1, level="中支撑")
            assert result2 is True, "更新目标支撑2失败"
            result3 = TrainingProgramRevisionPage().update_target_support(driver, index=1, level="低支撑")
            assert result3 is True, "更新目标支撑3失败"
            result4 = TrainingProgramRevisionPage().update_target_support(driver, index=1, level="中支撑")
            assert result4 is True, "更新目标支撑4失败"
            add_img_2_report(driver, "更新目标支撑")

        with allure.step("更新课程体系"):
            result = TrainingProgramRevisionPage().update_course_system(driver, course_name=course_info['课程名称'])
            add_img_2_report(driver, "更新课程体系")
            assert result is True, "更新课程体系失败"

        with allure.step("更新课程支撑"):
            result = TrainingProgramRevisionPage().update_course_support(driver, index=1, course_name=course_info['课程名称'], level="H")
            assert result is True, "更新课程支撑失败"
            result = TrainingProgramRevisionPage().update_course_support(driver, index=2, course_name=course_info['课程名称'], level="M")
            assert result is True, "更新课程支撑失败"
            add_img_2_report(driver, "更新课程支撑")
