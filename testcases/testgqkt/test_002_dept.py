# encoding: utf-8
# @File  : test_002_dept.py
# @Author: 孔敬淳
# @Date  : 2025/12/29/16:34
# @Desc  :
import allure
import pytest

from common.report_add_img import add_img_2_report
from testcases.helpers.test_context_helper import TestContextHelper
from common.yaml_config import GetConf
from page.department_manage.DeptListManagePage import DeptListManagePage


class TestInitializeDeptMajor:
    """创建院系测试"""

    @pytest.mark.run(order=120)
    @allure.story("创建院系")
    def test_001_create_dept(self, driver):
        """创建院系流程"""
        # 教务管理员账号
        dean_cms_user_info = GetConf().get_user_info("dean_cms")
        # 新建的院系信息
        dept_info = GetConf().get_info("department")

        # 使用TestContextHelper封装公共操作
        helper = TestContextHelper(driver)

        with allure.step("登录并进入院系列表管理"):
            result = helper.setup_context(
                user_info=dean_cms_user_info,
                menu_name="院系列表管理"
            )
            assert result is True, "登录或导航失败"

        with allure.step("创建院系"):
            result = DeptListManagePage().create_dept(driver, dept_info)
            add_img_2_report(driver, "创建院系")
            assert result is True, "创建院系失败"
