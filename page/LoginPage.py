# encoding: utf-8
# @File  : LoginPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/21:17
# @Desc  : 登录页面对象类，封装登录相关的页面操作方法
from selenium.webdriver.common.by import By

from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf


class LoginPage(LoginBase, ObjectMap):
    """登录页面类
    
    继承LoginBase和ObjectMap类，提供登录页面的元素操作方法
    """

    def login_input_value(self, driver, input_name, input_value):
        """在登录页面的输入框中输入内容
        
        Args:
            driver: WebDriver实例
            input_name: 输入框名称（账户、密码）
            input_value: 要输入的值
            
        Returns:
            元素操作结果
        """
        input_xpath = self.login_input(input_name)
        return self.element_input_value(driver, By.XPATH, input_xpath, input_value)

    def click_login_button(self, driver):
        """点击登录按钮
        
        Args:
            driver: WebDriver实例
            
        Returns:
            点击操作结果
        """
        return self.element_click(driver, By.XPATH, self.login_button())

    def user_login(self, driver, user_name):
        """用户登录操作
        
        Args:
            driver: WebDriver实例
            user_name: 用户名标识（用于从配置文件获取账号密码）
            
        Returns:
            登录操作结果
        """
        user_name, password = GetConf().get_username_password(user_name)
        self.element_to_url(driver, "login")
        self.login_input_value(driver, '账户', user_name)
        self.login_input_value(driver, '密码', password)
        return self.click_login_button(driver)
