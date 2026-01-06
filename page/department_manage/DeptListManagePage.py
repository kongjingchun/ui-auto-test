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
        xpath = self.dept_manage_iframe()
        log.info(f"切换到院系列表管理页面的iframe，xpath定位为：{xpath}")
        return self.switch_into_iframe(driver, By.XPATH, xpath)

    def click_new_dept_button(self, driver):
        """点击新建院系按钮

        Returns:
            点击操作结果
        """
        xpath = self.new_dept_button()
        log.info(f"点击新建院系按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def input_new_dept_input(self, driver, input_name, value):
        """输入新建院系信息

        Args:
            driver: WebDriver实例
            input_name: 输入框名称
            value: 输入的值
        Returns:
            输入操作结果
        """
        xpath = self.new_dept_input(input_name)
        log.info(f"输入新建院系信息：{input_name}为：{value}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, value)

    def click_new_dept_confirm_button(self, driver):
        """点击新建院系确认按钮

        Returns:
            点击操作结果
        """
        xpath = self.new_dept_confirm_button()
        log.info(f"点击新建院系确认按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def is_create_success_alert_display(self, driver):
        """查看创建成功提示框是否出现

        Returns:
            提示框是否出现
        """
        xpath = self.create_success_alert()
        log.info(f"查看创建成功提示框是否出现，xpath定位为：{xpath}")
        return self.element_is_display(driver, By.XPATH, xpath)

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

    def input_search_keyword(self, driver, keyword):
        """输入搜索关键词

        Args:
            driver: WebDriver实例
            keyword: 搜索关键词（院系名称或院系代码）

        Returns:
            输入操作结果
        """
        xpath = self.search_keyword_input()
        log.info(f"输入搜索关键词：{keyword}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, keyword)

    def hover_edit_button(self, driver, dept_code):
        """鼠标悬停编辑按钮（根据院系代码）

        Args:
            driver: WebDriver实例
            dept_code: 院系代码
        """
        xpath = self.edit_button_hover_location(dept_code)
        log.info(f"鼠标悬停编辑按钮（根据院系代码），xpath定位为：{xpath}")
        return self.element_hover(driver, By.XPATH, xpath)

    def click_edit_button_by_dept_code(self, driver, dept_code):
        """根据院系代码点击编辑按钮

        Args:
            driver: WebDriver实例
            dept_code: 院系代码

        Returns:
            点击操作结果
        """
        xpath = self.edit_button(dept_code)
        log.info(f"根据院系代码'{dept_code}'点击编辑按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

    def click_delete_button(self, driver):
        """点击删除院系按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.delete_button()
        log.info(f"点击删除院系按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

    def click_delete_confirm_button(self, driver):
        """点击删除确认按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.delete_confirm_button()
        log.info(f"点击删除确认按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

    def is_delete_success_alert_display(self, driver):
        """查看删除成功提示框是否出现

        Args:
            driver: WebDriver实例

        Returns:
            bool: True表示删除成功提示框出现，False表示未出现
        """
        xpath = self.delete_success_alert()
        log.info(f"查看删除成功提示框是否出现，xpath定位为：{xpath}")
        return self.element_is_display(driver, By.XPATH, xpath)

    def delete_dept_by_dept_code(self, driver, dept_code):
        """根据院系代码删除院系

        Args:
            driver: WebDriver实例
            dept_code: 院系代码

        Returns:
            bool: True表示删除成功，False表示删除失败
        """
        # 切换到iframe
        self.switch_2_dept_manage_iframe(driver)
        # 输入搜索关键词
        self.input_search_keyword(driver, dept_code)
        # 鼠标悬停编辑按钮
        self.hover_edit_button(driver, dept_code)
        # 点击编辑按钮
        self.click_edit_button_by_dept_code(driver, dept_code)
        # 点击删除按钮
        self.click_delete_button(driver)
        # 点击删除确认按钮
        self.click_delete_confirm_button(driver)
        # 断言删除成功提示框是否出现
        result = self.is_delete_success_alert_display(driver)
        # 切出iframe
        self.switch_out_iframe(driver)
        log.info(f"删除院系结果：{result}")
        return result
