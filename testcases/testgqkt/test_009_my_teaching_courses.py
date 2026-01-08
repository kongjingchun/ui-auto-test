# encoding: utf-8
# @File  : test_009_my_teaching_courses.py
# @Author:
# @Date  :
# @Desc  : 我教的课测试用例

import allure
import pytest

from common.report_add_img import add_img_2_report
from testcases.helpers.test_context_helper import TestContextHelper
from common.yaml_config import GetConf
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

        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录、切换教师身份、导航到我教的课"):
            result = helper.setup_context(user_info=prof_cms_user_info, role_name="教师", menu_name="我教的课")
            assert result is True, "登录、切换教师身份、导航到我教的课失败"

        with allure.step("根据课程名称点击课程卡片"):
            result = MyTeachingCoursesPage().click_course(driver, course_info['课程名称'])
            add_img_2_report(driver, "根据课程名称点击课程卡片")
            assert result is True, "根据课程名称点击课程卡片失败"
