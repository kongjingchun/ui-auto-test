# encoding: utf-8
# @File  : test_009_my_teaching_courses.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 我教的课测试用例，符合Selenium官方Page Object Model和pytest框架规范

import allure
import pytest

from common.report_add_img import add_img_2_report
from page.teacher_workbench.CourseWorkbenchPage import CourseWorkbenchPage
from page.teacher_workbench.ai_vertical_model.KnowledgeGraphPage import KnowledgeGraphPage
from testcases.helpers.test_context_helper import TestContextHelper
from common.yaml_config import GetConf
from page.teacher_workbench.MyTeachingCoursesPage import MyTeachingCoursesPage


class TestMyTeachingCourses:
    """我教的课测试类

    测试用例按照Selenium官方Page Object Model规范编写：
    1. 页面对象在测试用例中创建，driver通过pytest fixture注入
    2. 页面对象方法不包含driver参数
    3. 断言在测试用例中，不在页面对象中
    """

    @pytest.mark.run(order=200)
    @allure.story("添加知识图谱")
    def test_001_my_teaching_courses(self, driver):
        """
        测试添加知识图谱流程

        Args:
            driver: WebDriver实例（通过pytest fixture注入）

        Returns:
            None
        """
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
            my_teaching_courses_page = MyTeachingCoursesPage(driver)
            result = my_teaching_courses_page.click_course(course_info['课程名称'])
            add_img_2_report(driver, "根据课程名称点击课程卡片")
            assert result is True, "根据课程名称点击课程卡片失败"
        with allure.step("点击知识图谱菜单栏"):
            course_workbench_page = CourseWorkbenchPage(driver)
            course_workbench_page.click_left_menu("AI垂直模型")
            result = course_workbench_page.click_left_menu("知识图谱")
            add_img_2_report(driver, "点击知识图谱菜单栏")
            assert result is True, "点击知识图谱菜单栏失败"
        with allure.step("新建主图谱"):
            knowledge_graph_page = KnowledgeGraphPage(driver)
            result = knowledge_graph_page.create_main_graph(course_info['课程名称'], "课程知识图谱", "1.0", "课程知识图谱")
            add_img_2_report(driver, "新建主图谱")
            assert result is True, "新建主图谱失败"
