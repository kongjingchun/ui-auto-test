# encoding: utf-8
# @File  : test_005_create_course.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  :

import allure

from common.report_add_img import add_img_2_report
from common.yaml_config import GetConf
from page.LeftMenuPage import LeftMenuPage
from page.login.LoginPage import LoginPage
from page.dean_manage.CourseManagePage import CourseManagePage


class TestCreateCourse:
    """创建课程测试"""

    @allure.story("创建课程")
    def test_001_create_course(self, driver):
        """创建课程流程"""
        # 教务管理员账号
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # 新建的课程信息
        course_info = GetConf().get_info("course")

        with allure.step("登录教务管理员"):
            result = LoginPage().user_login(driver, dean_cms_user_info)
            add_img_2_report(driver, "登录教务管理员")
            assert result is True, "登录教务管理员失败"

        with allure.step("点击左侧课程管理菜单"):
            result = LeftMenuPage().click_two_level_menu(driver, "课程管理")
            add_img_2_report(driver, "点击左侧课程管理菜单")
            assert result is True, "点击左侧课程管理菜单失败"

        with allure.step("创建课程"):
            result = CourseManagePage().create_course(driver, course_info)
            add_img_2_report(driver, "创建课程")
            assert result is True, "创建课程失败"
