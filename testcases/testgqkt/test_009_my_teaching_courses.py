# encoding: utf-8
# @File  : test_009_my_teaching_courses.py
# @Author:
# @Date  :
# @Desc  : 我教的课测试用例

import allure
import pytest

from common.report_add_img import add_img_2_report
from common.yaml_config import GetConf
from page.LeftMenuPage import LeftMenuPage
from page.login.LoginPage import LoginPage
from page.teacher_workbench.MyTeachingCoursesPage import MyTeachingCoursesPage
from page.teacher_workbench.course_construction.AIVerticalModelPage import AIVerticalModelPage


class TestMyTeachingCourses:
    """我教的课测试"""

    @pytest.mark.run(order=200)
    @allure.story("我教的课")
    def test_001_my_teaching_courses(self, driver):
        """我教的课测试流程"""
        # 教师账号（可根据实际情况配置）
        # user_info = GetConf().get_user_info("teacher")

        with allure.step("登录教师账号"):
            # result = LoginPage().user_login(driver, user_info)
            # add_img_2_report(driver, "登录教师账号")
            # assert result is True, "登录教师账号失败"
            pass

        with allure.step("点击左侧我教的课菜单"):
            result = LeftMenuPage().click_two_level_menu(driver, "我教的课")
            add_img_2_report(driver, "点击左侧我教的课菜单")
            assert result is True, "点击左侧我教的课菜单失败"

        with allure.step("切换到课程建设-AI垂直模型"):
            result = AIVerticalModelPage().switch_into_ai_vertical_model_iframe(driver)
            add_img_2_report(driver, "切换到课程建设-AI垂直模型")
            assert result is True, "切换到课程建设-AI垂直模型失败"

