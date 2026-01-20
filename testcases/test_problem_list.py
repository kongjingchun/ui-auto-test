# coding:utf-8
import unittest

import allure
from common.report_add_img import add_img_2_report
from page.problems_list import ProblemListPage
from page.login_page import LoginPage
from common.yaml_config import GetConf


class TestProblemList():
    def test_03(self, driver):

        with allure.step("执行登录操作"):
            teacher_user_info = GetConf().get_user_info("teacher")
            login_page = LoginPage(driver)
            login_result = login_page.login_first(teacher_user_info["username"], teacher_user_info["password"])
            add_img_2_report(driver, "登录操作")
            assert login_result is True, "登录操作失败"

        with allure.step("执行题库检查"):
            pl = ProblemListPage(driver)
            pl.problem_check()
            result = pl.search_problem("资源")
            add_img_2_report(driver, "搜索操作")
            assert result is True, "搜索操作失败"

        with allure.step("新建习题"):
            pl.click_add_button()
            result = pl.add_subjective_problem("资源")
            add_img_2_report(driver, "添加主观题")
            assert result is True, "添加主观题失败"
