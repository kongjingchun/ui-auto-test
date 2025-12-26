# encoding: utf-8
# @File  : UserManagePage.py.py
# @Author: 孔敬淳
# @Date  : 2025/12/25/14:33
# @Desc  : 用户管理页面对象类，封装用户管理相关的页面操作方法
from time import sleep

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.academic_affairs.UserManageBase import UserManageBase
from common.yaml_config import GetConf
from logs.log import log


class UserManagePage(UserManageBase, ObjectMap):
    """用户管理页面类
    
    继承UserManageBase和ObjectMap类，提供用户管理页面的元素操作方法
    """

    def switch_2_user_manage_iframe(self, driver):
        """切换到用户管理页面的iframe

        Returns:
            切换操作结果
        """
        log.info("切换到用户管理页面的iframe")
        iframe_xpath = self.user_manage_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def switch_out_of_user_manage_iframe(self, driver):
        """退出用户管理页面的iframe

        Returns:
            退出操作结果
        """
        log.info("退出用户管理页面的iframe")
        return self.switch_out_iframe(driver)

    def move_add_user_button(self, driver):
        """鼠标悬停到创建按钮
        
        Args:
            driver: WebDriver实例
            
        Returns:
            悬停操作结果
        """
        log.info("鼠标悬停到手动创建按钮")
        xpath = self.add_user_button()
        return self.action_move_to_element(driver, By.XPATH, xpath)

    def click_add_user_role_select(self, driver, role_name):
        """点击选择创建的用户角色身份
        Args:
            driver: WebDriver实例
            role_name: 角色名称（如：创建教务管理员、创建教师、创建学生）
        Returns:
            点击操作结果
        """
        log.info("创建的角色身份为：" + role_name)
        xpath = self.add_user_role_select(role_name)
        return self.element_click(driver, By.XPATH, xpath)

    def input_user_value(self, driver, input_name, value):
        """输入用户信息"""
        log.info(f"输入用户信息：{input_name}为：{value}")
        xpath = self.input_xpath(input_name)
        return self.element_input_value(driver, By.XPATH, xpath, value)

    def click_submit_user_button(self, driver):
        """点击提交信息按钮
        Returns:
            点击操作结果
        """
        log.info("点击提交信息按钮")
        xpath = self.submit_user_button()
        return self.element_double_click(driver, By.XPATH, xpath)

    def create_user(self, driver, role_name, user):
        """创建用户
        Args:
            driver: WebDriver实例
            role_name: 角色名称（如：创建教务管理员、创建教师、创建学生）
            user:用户
        Returns:
            创建用户操作结果
        """
        user_name, user_code, user_phone, user_email = GetConf().get_user_info(user, "username", "user_code", "phone", "email")
        self.switch_2_user_manage_iframe(driver)
        self.move_add_user_button(driver)
        self.click_add_user_role_select(driver, role_name)
        self.input_user_value(driver, "姓名", str(user_name))
        self.input_user_value(driver, "工号", str(user_code))
        self.input_user_value(driver, "手机", str(user_phone))
        self.input_user_value(driver, "邮箱", str(user_email))
        self.click_submit_user_button(driver)
        self.switch_out_of_user_manage_iframe(driver)
