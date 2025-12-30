# encoding: utf-8
# @File  : test_003_creat_major.py.py
# @Author: 孔敬淳
# @Date  : 2025/12/30/16:21
# @Desc  :
import allure

from common.report_add_img import add_img_2_report
from common.yaml_config import GetConf
from page.LeftMenuPage import LeftMenuPage
from page.login.LoginPage import LoginPage
from page.major.MajorManagePage import MajorManagePage


class TestCreateMajor:
    """创建专业测试"""

    @allure.story("创建专业")
    def test_001_initialize_major(self, driver):
        """创建专业流程"""
        # 教务管理员账号
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # 新建的专业信息
        major_info = GetConf().get_info("major")

        with allure.step("登录教务管理员"):
            result = LoginPage().user_login(driver, dean_cms_user_info)
            add_img_2_report(driver, "登录教务管理员")
            assert result is True, "登录教务管理员失败"

        with allure.step("点击左侧专业管理菜单"):
            result = LeftMenuPage().click_two_level_menu(driver, "专业管理")
            add_img_2_report(driver, "点击左侧专业管理菜单")
            assert result is True, "点击左侧专业管理菜单失败"

        with allure.step("创建专业"):
            result = MajorManagePage().create_major(driver, major_info)
            add_img_2_report(driver, "创建专业")
            assert result is True, "创建专业失败"
