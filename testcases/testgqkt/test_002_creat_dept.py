# encoding: utf-8
# @File  : test_002_creat_dept.py.py
# @Author: 孔敬淳
# @Date  : 2025/12/29/16:34
# @Desc  :
import allure

from common.report_add_img import add_img_2_report
from common.yaml_config import GetConf
from page.login.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.department_manage.DeptListManagePage import DeptListManagePage


class TestInitializeDeptMajor:
    """初始学校院系、专业等流程"""

    @allure.story("初始化学校")
    def test_001_initialize_dept_major(self, driver):
        """
        初始学校院系、专业等流程
        :param driver: WebDriver实例
        :return: None
        """
        # 教务管理员账号
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # 新建的学院信息
        dept_info = GetConf().get_info("department")

        with allure.step("登录教务管理员"):
            result = LoginPage().user_login(driver, dean_cms_user_info)
            add_img_2_report(driver, "登录教务管理员")
            assert result is True, "登录教务管理员失败"

        with allure.step("进入院系列表管理"):
            result = LeftMenuPage().click_two_level_menu(driver, "院系列表管理")
            add_img_2_report(driver, "进入院系列表管理")
            assert result is True, "进入院系列表管理失败"

        with allure.step("创建院系"):
            result = DeptListManagePage().create_dept(driver, dept_info)
            add_img_2_report(driver, "创建院系")
            assert result is True, "创建院系失败"
