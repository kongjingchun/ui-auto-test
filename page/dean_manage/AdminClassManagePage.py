# encoding: utf-8
# @File  : AdminClassManagePage.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 行政班管理页面对象类，封装行政班管理相关的页面操作方法

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.dean_manage.AdminClassManageBase import AdminClassManageBase
from logs.log import log


class AdminClassManagePage(AdminClassManageBase, ObjectMap):
    """行政班管理页面类

    继承AdminClassManageBase和ObjectMap类，提供行政班管理页面的元素操作方法
    """

    def click_new_admin_class_button(self, driver):
        """点击新建行政班按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_admin_class_button()
        log.info(f"点击新建行政班按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def input_new_admin_class_input(self, driver, input_name, value):
        """输入新建行政班信息

        Args:
            driver: WebDriver实例
            input_name: 输入框名称（如：'名称'、'编号'、'描述'）
            value: 输入的值

        Returns:
            输入操作结果
        """
        xpath = self.new_admin_class_input(input_name)
        log.info(f"输入新建行政班信息：{input_name}为：{value}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, value)

    def click_new_admin_class_dept_dropdown(self, driver):
        """点击所属学院下拉框

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_admin_class_dept_dropdown()
        log.info(f"点击所属学院下拉框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_admin_class_dept_dropdown_option(self, driver, dept_name):
        """点击所属学院下拉框选项

        Args:
            driver: WebDriver实例
            dept_name: 学院名称

        Returns:
            点击操作结果
        """
        xpath = self.new_admin_class_dept_dropdown_option(dept_name)
        log.info(f"点击所属学院下拉框选项：{dept_name}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)
        # 点击后等待下拉菜单关闭
        import time
        time.sleep(0.5)
        return result

    def click_new_admin_class_major_dropdown(self, driver):
        """点击所属专业下拉框

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_admin_class_major_dropdown()
        log.info(f"点击所属专业下拉框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_admin_class_major_dropdown_option(self, driver, major_name):
        """点击所属专业下拉框选项

        Args:
            driver: WebDriver实例
            major_name: 专业名称

        Returns:
            点击操作结果
        """
        xpath = self.new_admin_class_major_dropdown_option(major_name)
        log.info(f"点击所属专业下拉框选项：{major_name}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)
        # 点击后等待下拉菜单关闭
        import time
        time.sleep(0.5)
        return result

    def click_new_admin_class_grade_dropdown(self, driver):
        """点击年级下拉框

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_admin_class_grade_dropdown()
        log.info(f"点击年级下拉框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_admin_class_grade_dropdown_option(self, driver, grade="2025级"):
        """点击年级下拉框选项

        Args:
            driver: WebDriver实例
            grade: 年级，默认为2025级（传入参数必须后面带级字，如2025级，2026级）

        Returns:
            点击操作结果
        """
        xpath = self.new_admin_class_grade_dropdown_option(grade)
        log.info(f"点击年级下拉框选项：{grade}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)
        # 点击后等待下拉菜单关闭
        import time
        time.sleep(0.5)
        return result

    def click_new_admin_class_confirm_button(self, driver):
        """点击新建行政班确认按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_admin_class_confirm_button()
        log.info(f"点击新建行政班确认按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def is_create_success_alert_display(self, driver):
        """查看创建成功提示框是否出现

        Args:
            driver: WebDriver实例

        Returns:
            bool: True表示创建成功提示框出现，False表示未出现
        """
        xpath = self.create_success_alert()
        log.info(f"查看创建成功提示框是否出现，xpath定位为：{xpath}")
        return self.element_is_display(driver, By.XPATH, xpath)

    def create_admin_class(self, driver, admin_class_info=None):
        """创建行政班

        Args:
            driver: WebDriver实例
            admin_class_info: 行政班信息

        Returns:
            bool: True表示创建成功，False表示创建失败
        """
        self.switch_into_iframe(driver, By.XPATH, self.admin_class_manage_iframe())
        self.click_new_admin_class_button(driver)
        self.input_new_admin_class_input(driver, "名称", admin_class_info['行政班名称'])
        self.input_new_admin_class_input(driver, "编号", admin_class_info['行政班编号'])
        self.click_new_admin_class_dept_dropdown(driver)
        self.click_new_admin_class_dept_dropdown_option(driver, admin_class_info['所属学院'])
        self.click_new_admin_class_major_dropdown(driver)
        self.click_new_admin_class_major_dropdown_option(driver, admin_class_info['所属专业'])
        self.click_new_admin_class_grade_dropdown(driver)
        self.click_new_admin_class_grade_dropdown_option(driver, admin_class_info['年级'])
        self.input_new_admin_class_input(driver, "描述", admin_class_info['行政班描述'])
        self.click_new_admin_class_confirm_button(driver)
        result = self.is_create_success_alert_display(driver)
        self.switch_out_iframe(driver)
        log.info(f"创建行政班结果：{result}")
        return result
