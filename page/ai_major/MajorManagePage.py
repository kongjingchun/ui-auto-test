# encoding: utf-8
# @File  : MajorManagePage.py.py
# @Author: 孔敬淳
# @Date  : 2025/12/30/16:23
# @Desc  :
from time import sleep

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.ai_major.MajorManageBase import MajorManageBase
from logs.log import log


class MajorManagePage(MajorManageBase, ObjectMap):
    """专业管理页面类

    继承MajorManageBase和ObjectMap类，提供专业管理页面元素操作方法
    """

    def click_new_major_button(self, driver):
        """点击新建专业按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_major_button()
        log.info(f"点击新建专业按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def input_new_major_input(self, driver, input_name, value):
        """输入新建专业信息

        Args:
            driver: WebDriver实例
            input_name: 输入框名称
            value: 输入的值
        Returns:
            输入操作结果
        """
        xpath = self.new_major_input(input_name)
        log.info(f"输入新建专业信息：{input_name}为：{value}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, value)

    def click_new_major_belong_dep_dropdown(self, driver):
        """点击所属院系下拉框

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_major_belong_dep_dropdown()
        log.info(f"点击所属院系下拉框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_major_belong_dep_dropdown_option(self, driver, dep_name):
        """点击所属院系下拉框选项

        Args:
            driver: WebDriver实例
            dep_name: 院系名称
        Returns:
            点击操作结果
        """
        xpath = self.new_major_belong_dep_dropdown_option(dep_name)
        log.info(f"点击所属院系下拉框选项：{dep_name}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)
        # 点击后等待下拉菜单关闭
        sleep(0.5)
        return result

    def click_new_major_belong_prof_dropdown(self, driver):
        """点击专业负责人下拉框

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_major_belong_prof_dropdown()
        log.info(f"点击专业负责人下拉框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_major_belong_prof_dropdown_option(self, driver, prof_name):
        """点击专业负责人下拉框选项

        Args:
            driver: WebDriver实例
            prof_name: 专业负责人名称
        Returns:
            点击操作结果
        """
        xpath = self.new_major_belong_prof_dropdown_option(prof_name)
        log.info(f"点击专业负责人下拉框选项：{prof_name}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)
        # 点击后等待下拉菜单关闭
        sleep(0.5)
        return result

    def click_new_major_build_level_radio(self, driver, level):
        """点击建设层次单选框

        Args:
            driver: WebDriver实例
            level:建设层次
        Returns:
            点击操作结果
        """
        xpath = self.new_major_build_level_radio(level)
        log.info(f"点击建设层次单选框：{level}，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_major_feature_checkbox(self, driver, feature="国家级特色专业"):
        """点击特色专业复选框

        Args:
            driver: WebDriver实例
            feature: 特色专业
        Returns:
            点击操作结果
        """
        xpath = self.new_major_feature_checkbox(feature)
        log.info(f"点击特色专业复选框：{feature}，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_major_confirm_button(self, driver):
        """点击新建专业确认按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_major_confirm_button()
        log.info(f"点击新建专业确认按钮，xpath定位为：{xpath}")
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

    def create_major(self, driver, major_info=None):
        """创建专业

        Args:
            driver: WebDriver实例
            major_info: 专业信息

        Returns:
            bool: True表示创建成功，False表示创建失败
        """
        # 切换到iframe
        self.switch_into_iframe(driver, By.XPATH, self.major_manage_iframe())

        # 点击新建专业按钮
        self.click_new_major_button(driver)

        # 从上到下设置新建信息
        # 1. 专业名称
        self.input_new_major_input(driver, "名称", major_info['专业名称'])

        # 2. 学校专业代码
        self.input_new_major_input(driver, "学校专业代码", major_info['学校专业代码'])

        # 3. 国家专业代码
        self.input_new_major_input(driver, "国家专业代码", major_info['国家专业代码'])

        # 4. 所属院系
        self.click_new_major_belong_dep_dropdown(driver)
        sleep(0.5)
        self.click_new_major_belong_dep_dropdown_option(driver, major_info['所属院系'])

        # 5. 专业负责人
        self.click_new_major_belong_prof_dropdown(driver)
        self.click_new_major_belong_prof_dropdown_option(driver, major_info['专业负责人'])

        # 6. 专业建设层次
        self.click_new_major_build_level_radio(driver, major_info['专业建设层次'])

        # 7. 专业特色标签（循环选择多个特色标签）
        for feature in major_info['专业特色标签']:
            self.click_new_major_feature_checkbox(driver, feature)

        # 点击确定按钮
        self.click_new_major_confirm_button(driver)

        # 断言创建成功提示框是否出现
        result = self.is_create_success_alert_display(driver)

        # 切出iframe
        self.switch_out_iframe(driver)

        log.info(f"创建专业结果：{result}")
        return result
