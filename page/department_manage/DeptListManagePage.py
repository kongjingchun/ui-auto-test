# encoding: utf-8
# @File  : DeptListManagePage.py.py
# @Author: 孔敬淳
# @Date  : 2025/12/29/16:27
# @Desc  : 院系列表管理
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.department_manage.DeptListManageBase import DeptListManageBase
from logs.log import log


class DeptListManagePage(DeptListManageBase, ObjectMap):
    """院系列表管理页面类

    继承DepListManageBase和ObjectMap类，提供院系列表管理页面元素操作方法
    """

    def switch_2_dept_manage_iframe(self, driver):
        """切换到院系列表管理页面的iframe

        Returns:
            切换操作结果
        """
        log.info("切换到院系列表管理页面的iframe")
        return self.switch_into_iframe(driver, By.XPATH, self.dept_manage_iframe())

    def click_new_dept_button(self, driver):
        """点击新建院系按钮

        Returns:
            点击操作结果
        """
        log.info("点击新建院系按钮")
        return self.element_click(driver, By.XPATH, self.new_dept_button())

    def input_new_dept_input(self, driver, input_name, value):
        """输入新建院系信息

        Args:
            driver: WebDriver实例
            input_name: 输入框名称
            value: 输入的值
        Returns:
            输入操作结果
        """

        log.info(f"输入新建院系信息：{input_name}为：{value}")
        return self.element_input_value(driver, By.XPATH, self.new_dept_input(input_name), value)

    def click_new_dept_confirm_button(self, driver):
        """点击新建院系确认按钮

        Returns:
            点击操作结果
        """
        log.info("点击新建院系确认按钮")
        return self.element_click(driver, By.XPATH, self.new_dept_confirm_button())

    def is_create_success_alert_display(self, driver):
        """查看创建成功提示框是否出现

        Returns:
            提示框是否出现
        """
        log.info("查看创建成功提示框是否出现")
        return self.element_is_display(driver, By.XPATH, self.create_success_alert())

    def create_dept(self, driver, dept_info):
        """创建院系

        Args:
            driver: WebDriver实例
            dept_info: 院系信息
        Returns:
            创建操作结果
        """
        self.switch_2_dept_manage_iframe(driver)
        self.click_new_dept_button(driver)
        for input_name, value in dept_info.items():
            self.input_new_dept_input(driver, input_name, value)
        self.click_new_dept_confirm_button(driver)
        result = self.is_create_success_alert_display(driver)
        self.switch_out_iframe(driver)
        log.info("创建院系结果：" + str(result))
        return result
