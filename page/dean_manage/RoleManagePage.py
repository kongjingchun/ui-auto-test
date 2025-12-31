# encoding: utf-8
# @File  : RoleManagePage.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 角色管理页面对象类，封装角色管理相关的页面操作方法

from time import sleep

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.dean_manage.RoleManageBase import RoleManageBase
from logs.log import log


class RoleManagePage(RoleManageBase, ObjectMap):
    """角色管理页面类

    继承RoleManageBase和ObjectMap类，提供角色管理页面的元素操作方法
    """

    def click_assign_role_button(self, driver, role_name):
        """点击分配角色按钮

        Args:
            driver: WebDriver实例
            role_name: 角色名称

        Returns:
            点击操作结果
        """
        xpath = self.assign_role_button(role_name)
        log.info(f"点击分配角色按钮，角色名称：{role_name}，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def input_user_search(self, driver, user_name):
        """输入用户搜索信息

        Args:
            driver: WebDriver实例
            user_id: 用户ID

        Returns:
            输入操作结果
        """
        xpath = self.user_search_input()
        log.info(f"输入用户搜索信息：{user_name}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, user_name)

    def click_user_checkbox(self, driver, user_name):
        """勾选用户复选框

        Args:
            driver: WebDriver实例
            user_name: 用户名称

        Returns:
            点击操作结果
        """
        xpath = self.user_checkbox(user_name)
        log.info(f"勾选用户复选框，用户名称：{user_name}，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_assign_role_confirm_button(self, driver):
        """点击分配角色确认按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.assign_role_confirm_button()
        log.info(f"点击分配角色确认按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def is_assign_role_success_alert_display(self, driver):
        """判断分配角色成功提示框是否出现

        Args:
            driver: WebDriver实例

        Returns:
            bool: True表示分配成功提示框出现，False表示未出现
        """
        xpath = self.assign_role_success_alert()
        log.info(f"判断分配角色成功提示框是否出现，xpath定位为：{xpath}")
        return self.element_is_display(driver, By.XPATH, xpath)

    def assign_role_to_user(self, driver, role_name, user_name=None):
        """分配角色给用户

        Args:
            driver: WebDriver实例
            role_name: 角色名称
            user_id: 用户ID（可选，用于搜索用户）
            user_name: 用户名称（必填，用于勾选用户）

        Returns:
            bool: True表示分配成功，False表示分配失败
        """
        self.switch_into_iframe(driver, By.XPATH, self.role_manage_iframe())
        self.click_assign_role_button(driver, role_name)
        self.input_user_search(driver, user_name)
        self.click_user_checkbox(driver, user_name)
        self.click_assign_role_confirm_button(driver)
        result = self.is_assign_role_success_alert_display(driver)
        self.switch_out_iframe(driver)
        log.info(f"分配角色 {role_name} 给用户 {user_name} 完成")
        return result
