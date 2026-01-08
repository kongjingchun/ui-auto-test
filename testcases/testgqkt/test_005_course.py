# encoding: utf-8
# @File  : test_005_course.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  :

import allure
import pytest

from common.report_add_img import add_img_2_report
from testcases.helpers.test_context_helper import TestContextHelper
from common.yaml_config import GetConf
from page.dean_manage.CourseManagePage import CourseManagePage


class TestCourse:
    """创建课程测试"""

    @pytest.mark.run(order=150)
    @allure.story("创建课程")
    def test_001_create_course(self, driver):
        """创建课程流程"""
        # 教务管理员账号
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # 新建的课程信息
        course_info = GetConf().get_info("course")

        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录并进入课程管理"):
            result = helper.setup_context(
                user_info=dean_cms_user_info,
                menu_name="课程管理"
            )
            assert result is True, "登录或导航失败"

        with allure.step("创建课程"):
            result = CourseManagePage().create_course(driver, course_info)
            add_img_2_report(driver, "创建课程")
            assert result is True, "创建课程失败"
