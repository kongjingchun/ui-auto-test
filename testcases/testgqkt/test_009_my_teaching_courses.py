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
from page.TopMenuPage import TopMenuPage
from page.login.LoginPage import LoginPage
from page.teacher_workbench.MyTeachingCoursesPage import MyTeachingCoursesPage
from page.teacher_workbench.course_construction.AIVerticalModelPage import AIVerticalModelPage


class TestMyTeachingCourses:
    """我教的课测试"""

    @pytest.mark.run(order=200)
    @allure.story("添加知识图谱")
    def test_001_my_teaching_courses(self, driver):
        """添加知识图谱测试流程"""
        # 专业管理员账号
        prof_cms_user_info = GetConf().get_user_info("prof_cms")
        # 课程信息
        course_info = GetConf().get_info("course")
        with allure.step("登录专业管理员账号"):
            result = LoginPage().user_login(driver, prof_cms_user_info)
            add_img_2_report(driver, "登录账号")
            assert result is True, "登录账号失败"
            pass

        with allure.step("切换教师身份"):
            result = TopMenuPage().switch_role(driver, "教师")
            add_img_2_report(driver, "切换教师身份")
            assert result is True, "切换教师身份失败"

        with allure.step("点击左侧我教的课菜单"):
            result = LeftMenuPage().click_two_level_menu(driver, "我教的课")
            add_img_2_report(driver, "点击左侧我教的课菜单")
            assert result is True, "点击左侧我教的课菜单失败"

        with allure.step("根据课程名称点击课程卡片"):
            result = MyTeachingCoursesPage().click_course(driver, course_info['课程名称'])
            add_img_2_report(driver, "根据课程名称点击课程卡片")
            assert result is True, "根据课程名称点击课程卡片失败"
