# encoding: utf-8
# @File  : AdminClassManagePage.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 行政班管理页面对象类，封装行政班管理相关的页面操作方法

from time import sleep

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.dean_manage.AdminClassManageBase import AdminClassManageBase
from logs.log import log


class AdminClassManagePage(AdminClassManageBase, ObjectMap):
    """行政班管理页面类

    继承AdminClassManageBase和ObjectMap类，提供行政班管理页面的元素操作方法
    """
    # iframe

    def switch_into_admin_class_manage_iframe(self, driver):
        """切换到行政班管理iframe

        Args:
            driver: WebDriver实例

        Returns:
            切换操作结果
        """
        xpath = self.admin_class_manage_iframe()
        log.info(f"切换到行政班管理iframe，xpath定位为：{xpath}")
        return self.switch_into_iframe(driver, By.XPATH, xpath)

    def input_search_keyword(self, driver, keyword):
        """输入搜索关键词

        Args:
            driver: WebDriver实例
            keyword: 搜索关键词（行政班名称或行政班编号）

        Returns:
            输入操作结果
        """
        xpath = self.search_keyword_input()
        log.info(f"输入搜索关键词：{keyword}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, keyword)

    def click_search_button(self, driver):
        """点击搜索按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.search_button()
        log.info(f"点击搜索按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

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
        return self.element_input_value(driver, By.XPATH, xpath, value, need_enter=True)

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
        sleep(0.5)
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
        sleep(0.5)
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
        sleep(0.5)
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

    def click_operation_button_by_admin_class_name(self, driver, admin_class_name):
        """根据行政班名称点击操作按钮

        Args:
            driver: WebDriver实例
            admin_class_name: 行政班名称

        Returns:
            点击操作结果
        """
        xpath = self.operation_button_by_admin_class_name(admin_class_name)
        log.info(f"根据行政班名称'{admin_class_name}'点击操作按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

    def click_delete_li(self, driver):
        """点击删除下拉选项

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.delete_li()
        log.info(f"点击删除下拉选项，xpath定位为：{xpath}")
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

    def create_admin_class(self, driver, admin_class_info=None):
        """创建行政班

        Args:
            driver: WebDriver实例
            admin_class_info: 行政班信息

        Returns:
            bool: True表示创建成功，False表示创建失败
        """
        # 切换到iframe
        self.switch_into_admin_class_manage_iframe(driver)

        # 点击新建行政班按钮
        self.click_new_admin_class_button(driver)

        # 从上到下设置新建信息
        # 1. 行政班名称
        self.input_new_admin_class_input(driver, "名称", admin_class_info['行政班名称'])

        # 2. 行政班编号
        self.input_new_admin_class_input(driver, "编号", admin_class_info['行政班编号'])

        # 3. 所属学院
        self.click_new_admin_class_dept_dropdown(driver)
        self.click_new_admin_class_dept_dropdown_option(driver, admin_class_info['所属学院'])

        # 4. 所属专业
        self.click_new_admin_class_major_dropdown(driver)
        self.click_new_admin_class_major_dropdown_option(driver, admin_class_info['所属专业'])

        # 5. 年级
        self.click_new_admin_class_grade_dropdown(driver)
        self.click_new_admin_class_grade_dropdown_option(driver, admin_class_info['年级'])

        # 6. 行政班描述
        self.input_new_admin_class_input(driver, "描述", admin_class_info['行政班描述'])

        # 点击确定按钮
        self.click_new_admin_class_confirm_button(driver)

        # 断言创建成功提示框是否出现
        result = self.is_create_success_alert_display(driver)

        # 切出iframe
        self.switch_out_iframe(driver)

        log.info(f"创建行政班结果：{result}")
        return result

    def delete_admin_class_by_admin_class_name(self, driver, admin_class_name):
        """根据行政班名称删除行政班

        Args:
            driver: WebDriver实例
            admin_class_name: 行政班名称

        Returns:
            bool: True表示删除成功，False表示删除失败
        """
        # 切换到iframe
        self.switch_into_iframe(driver, By.XPATH, self.admin_class_manage_iframe())
        # 输入搜索关键词
        self.input_search_keyword(driver, admin_class_name)
        # 点击搜索按钮
        self.click_search_button(driver)
        # 根据行政班名称点击操作按钮
        self.click_operation_button_by_admin_class_name(driver, admin_class_name)
        # 点击删除下拉选项
        self.click_delete_li(driver)
        # 点击删除确认按钮
        self.click_delete_confirm_button(driver)
        # 断言删除成功提示框是否出现
        result = self.is_delete_success_alert_display(driver)
        # 切出iframe
        self.switch_out_iframe(driver)
        log.info(f"删除行政班结果：{result}")
        return result
