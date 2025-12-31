# encoding: utf-8
# @File  : CourseManagePage.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 课程管理页面对象类，封装课程管理相关的页面操作方法

from time import sleep

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.dean_manage.CourseManageBase import CourseManageBase
from logs.log import log


class CourseManagePage(CourseManageBase, ObjectMap):
    """课程管理页面类

    继承CourseManageBase和ObjectMap类，提供课程管理页面的元素操作方法
    """

    def click_new_course_button(self, driver):
        """点击新建课程按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_course_button()
        log.info(f"点击新建课程按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def input_new_course_input(self, driver, input_name, value):
        """输入新建课程信息

        Args:
            driver: WebDriver实例
            input_name: 输入框名称（如：'名称'、'代码'）
            value: 输入的值

        Returns:
            输入操作结果
        """
        xpath = self.new_course_input(input_name)
        log.info(f"输入新建课程信息：{input_name}为：{value}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, value)

    def click_new_course_dept_dropdown(self, driver):
        """点击所属学院下拉框

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_course_dept_dropdown()
        log.info(f"点击所属学院下拉框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_course_dept_dropdown_option(self, driver, dept_name):
        """点击所属学院下拉框选项

        Args:
            driver: WebDriver实例
            dept_name: 学院名称

        Returns:
            点击操作结果
        """
        xpath = self.new_course_dept_dropdown_option(dept_name)
        log.info(f"点击所属学院下拉框选项：{dept_name}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)
        # 点击后等待下拉菜单关闭
        sleep(0.5)
        return result

    def click_new_course_responsible_person_dropdown(self, driver):
        """点击课程负责人下拉框

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_course_responsible_person_dropdown()
        log.info(f"点击课程负责人下拉框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_course_responsible_person_dropdown_option(self, driver, prof_name):
        """点击课程负责人下拉框选项

        Args:
            driver: WebDriver实例
            prof_name: 课程负责人名称

        Returns:
            点击操作结果
        """
        xpath = self.new_course_responsible_person_dropdown_option(prof_name)
        log.info(f"点击课程负责人下拉框选项：{prof_name}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)
        # 点击后等待下拉菜单关闭
        sleep(0.5)
        return result

    def click_new_course_first_class_switch(self, driver):
        """点击是否一流课程开关

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_course_first_class_switch()
        log.info(f"点击是否一流课程开关，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_course_confirm_button(self, driver):
        """点击新建课程确认按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_course_confirm_button()
        log.info(f"点击新建课程确认按钮，xpath定位为：{xpath}")
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

    def create_course(self, driver, course_info=None):
        """创建课程

        Args:
            driver: WebDriver实例
            course_info: 课程信息

        Returns:
            bool: True表示创建成功，False表示创建失败
        """
        self.switch_into_iframe(driver, By.XPATH, self.course_manage_iframe())
        self.click_new_course_button(driver)
        sleep(1)
        self.input_new_course_input(driver, "名称", course_info['课程名称'])
        self.input_new_course_input(driver, "代码", course_info['课程代码'])
        # 如果存在课程描述，则输入
        if course_info.get('课程描述'):
            self.input_new_course_input(driver, "描述", course_info['课程描述'])
        self.click_new_course_dept_dropdown(driver)
        sleep(1)
        self.click_new_course_dept_dropdown_option(driver, course_info['所属学院'])
        self.click_new_course_responsible_person_dropdown(driver)
        sleep(1)
        self.click_new_course_responsible_person_dropdown_option(driver, course_info['课程负责人'])
        # 如果是否一流课程为true，则打开开关
        if course_info.get('是否一流课程', False):
            self.click_new_course_first_class_switch(driver)
        # 课程图片不上传，跳过
        self.click_new_course_confirm_button(driver)
        sleep(1)
        result = self.is_create_success_alert_display(driver)
        self.switch_out_iframe(driver)
        log.info(f"创建课程结果：{result}")
        return result
