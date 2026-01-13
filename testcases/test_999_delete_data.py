# encoding: utf-8
# @File  : test_008_delete_data.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 删除数据测试用例

import allure
import pytest

from common.report_add_img import add_img_2_report
from testcases.helpers.test_context_helper import TestContextHelper
from common.yaml_config import GetConf
from page.ai_major.MajorManagePage import MajorManagePage
from page.ai_major.TrainingProgramManage.TrainingProgramManagePage import TrainingProgramManagePage
from page.cms.CmsUserManagePage import CmsUserManage
from page.dean_manage.AdminClassManagePage import AdminClassManagePage
from page.dean_manage.CourseManagePage import CourseManagePage
from page.dean_manage.UserManagePage import UserManagePage
from page.department_manage.DeptListManagePage import DeptListManagePage


# @pytest.mark.skip(reason="跳过删除数据测试用例")
class TestDeleteData:
    """删除数据测试"""

    @pytest.mark.run(order=610)
    @allure.story("删除培养方案")
    def test_001_delete_training_program(self, driver):
        """删除培养方案流程"""
        # 专业管理员账号
        prof_cms_user_info = GetConf().get_user_info("prof_cms")
        # 培养方案信息
        training_program_info = GetConf().get_info("training_program")

        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录并进入培养方案管理"):
            result = helper.setup_context(
                user_info=prof_cms_user_info,
                role_name="专业管理员",
                menu_name="培养方案管理"
            )
            assert result is True, "登录或导航失败"

        with allure.step("删除培养方案"):
            result = TrainingProgramManagePage().delete_training_program_by_program_name(
                driver, training_program_info['方案名称'])
            add_img_2_report(driver, "删除培养方案")
            assert result is True, "删除培养方案失败"

    @pytest.mark.run(order=620)
    @allure.story("删除课程")
    def test_002_delete_course(self, driver):
        """删除课程流程"""
        # 教务管理员账号
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # 课程信息
        course_info = GetConf().get_info("course")

        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录并进入课程管理"):
            result = helper.setup_context(
                user_info=dean_cms_user_info,
                menu_name="课程管理"
            )
            assert result is True, "登录或导航失败"

        with allure.step("删除课程"):
            result = CourseManagePage().delete_course_by_course_code(
                driver, course_info['课程代码'])
            add_img_2_report(driver, "删除课程")
            assert result is True, "删除课程失败"

    @pytest.mark.run(order=630)
    @allure.story("删除行政班")
    def test_003_delete_admin_class(self, driver):
        """删除行政班流程"""
        # 教务管理员账号
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # 行政班信息
        admin_class_info = GetConf().get_info("admin_class")

        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录并进入行政班管理"):
            result = helper.setup_context(
                user_info=dean_cms_user_info,
                menu_name="行政班管理"
            )
            assert result is True, "登录或导航失败"

        with allure.step("删除行政班"):
            result = AdminClassManagePage().delete_admin_class_by_admin_class_name(driver, admin_class_info['行政班名称'])
            add_img_2_report(driver, "删除行政班")
            assert result is True, "删除行政班失败"

    @pytest.mark.run(order=640)
    @allure.story("删除专业")
    def test_004_delete_major(self, driver):
        """删除专业流程"""
        # 教务管理员账号
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # 专业信息
        major_info = GetConf().get_info("major")

        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录并进入专业管理"):
            result = helper.setup_context(
                user_info=dean_cms_user_info,
                menu_name="专业管理"
            )
            assert result is True, "登录或导航失败"

        with allure.step("删除专业"):
            result = MajorManagePage().delete_major_by_major_name(driver, major_info['专业名称'])
            add_img_2_report(driver, "删除专业")
            assert result is True, "删除专业失败"

    @pytest.mark.run(order=650)
    @allure.story("删除院系")
    def test_005_delete_dept(self, driver):
        """删除院系流程"""
        # 教务管理员账号
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # 院系信息
        dept_info = GetConf().get_info("department")

        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录并进入院系列表管理"):
            result = helper.setup_context(
                user_info=dean_cms_user_info,
                menu_name="院系列表管理"
            )
            assert result is True, "登录或导航失败"

        with allure.step("删除院系"):
            result = DeptListManagePage().delete_dept_by_dept_code(driver, dept_info['院系代码'])
            add_img_2_report(driver, "删除院系")
            assert result is True, "删除院系失败"

    # 删除用户
    @pytest.mark.run(order=660)
    @allure.story("删除用户")
    def test_006_delete_user(self, driver):
        """删除用户流程"""
        # 学校名称
        school_name = GetConf().get_school_name()
        # 初始管理员信息（账密）
        initial_admin = GetConf().get_user_info("initial_admin")
        # 教务管理员信息
        dean_user_info = GetConf().get_user_info("dean")
        # 专业负责人信息
        prof_user_info = GetConf().get_user_info("prof")

        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录、切换学校并进入用户管理"):
            result = helper.setup_context(
                user_info=initial_admin,
                school_name=school_name,
                menu_name="用户管理"
            )
            assert result is True, "设置用户上下文失败"

        with allure.step("删除专业管理员"):
            result = UserManagePage().delete_user_by_code(driver, prof_user_info['工号'])
            add_img_2_report(driver, "删除专业管理员")
            assert result is True, "删除专业管理员失败"

        with allure.step("删除教务管理员"):
            result = UserManagePage().delete_user_by_code(driver, dean_user_info['工号'])
            add_img_2_report(driver, "删除教务管理员")
            assert result is True, "删除教务管理员失败"

    @pytest.mark.skip_local  # 本地部署环境下跳过
    @pytest.mark.run(order=670)
    @allure.story("删除cms用户")
    def test_007_delete_prof_cms_user(self, driver):
        """删除cms用户流程"""
        # 初始管理员信息（账密）
        initial_admin = GetConf().get_user_info("initial_admin")
        # CMS教务管理员信息
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # CMS专业负责人信息
        prof_cms_user_info = GetConf().get_user_info("prof_cms")
        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录、切换到CMS并进入全部用户管理"):
            result = helper.setup_context(
                user_info=initial_admin,
                school_name="CMS管理系统",
                menu_name="全部用户管理"
            )
            assert result is True, "设置用户上下文失败"

        with allure.step("删除CMS专业管理员"):
            result = CmsUserManage().delete_cms_user_by_username(driver, prof_cms_user_info['username'])
            add_img_2_report(driver, "删除CMS专业管理员")
            assert result is True, "删除CMS专业管理员失败"

        with allure.step("删除CMS教务管理员"):
            result = CmsUserManage().delete_cms_user_by_username(driver, dean_cms_user_info['username'])
            add_img_2_report(driver, "删除CMS教务管理员")
            assert result is True, "删除CMS教务管理员失败"
