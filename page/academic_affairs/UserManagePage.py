# encoding: utf-8
# @File  : UserManagePage.py.py
# @Author: 孔敬淳
# @Date  : 2025/12/25/14:33
# @Desc  : 用户管理页面对象类，封装用户管理相关的页面操作方法
from time import sleep

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.academic_affairs.UserManageBase import UserManageBase
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

    # 点击提交信息按钮
    def click_submit_user_button(self, driver):
        """点击提交信息按钮
        Returns:
            点击操作结果
        """
        log.info("点击提交信息按钮")
        xpath = self.submit_user_button()
        return self.element_click(driver, By.XPATH, xpath)


    def create_user(self, driver, role_name, user_name, user_code, user_phone, user_email):
        """创建用户
        Args:
            driver: WebDriver实例
            role_name: 角色名称（如：创建教务管理员、创建教师、创建学生）
            user_name: 用户姓名
            user_code: 用户学号
            user_phone: 用户手机号
            user_email: 用户邮箱
        Returns:
            创建用户操作结果
        """
        log.info("创建" + role_name + "用户信息为：用户姓名：" + user_name + "，用户工号：" + user_code + "，用户手机号：" + user_phone + "，用户邮箱：" + user_email)
        self.switch_2_user_manage_iframe(driver)
        self.move_add_user_button(driver)
        self.click_add_user_role_select(driver, role_name)
        self.element_input_value(driver, By.XPATH, self.input_user_value("姓名"), user_name)
        self.element_input_value(driver, By.XPATH, self.input_user_value("工号"), user_code)
        self.element_input_value(driver, By.XPATH, self.input_user_value("手机"), user_phone)
        self.element_input_value(driver, By.XPATH, self.input_user_value("邮箱"), user_email)
        # xpath = self.submit_user_button()
        # element = self.element_get(driver, By.XPATH, xpath)
        # # sleep(2)
        # # element.click()
        # # sleep(2)
        # # element.click()
        # sleep(2)
        # # element.click()
        log.info(self.click_submit_user_button(driver))
        log.info(self.click_submit_user_button(driver))
        sleep(3)
