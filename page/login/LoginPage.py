# encoding: utf-8
# @File  : LoginPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/21:17
# @Desc  : 登录页面对象类，封装登录相关的页面操作方法
from selenium.webdriver.common.by import By

from base.login.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from logs.log import log


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
        log.info(f"在登录页面输入{input_name}：{input_value}，xpath定位为：{input_xpath}")
        return self.element_input_value(driver, By.XPATH, input_xpath, input_value)

    def click_login_button(self, driver):
        """点击登录按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.login_button()
        log.info(f"点击登录按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def user_login(self, driver, user_info):
        """用户登录操作

        Args:
            driver: WebDriver实例
            user_name: 用户名标识（用于从配置文件获取账号密码）

        Returns:
            登录操作结果
        """
        username = user_info["username"]
        password = user_info["password"]
        log.info(f"用户登录：{username}")
        self.element_to_url(driver, "login")
        self.login_input_value(driver, '账户', username)
        self.login_input_value(driver, '密码', password)
        return self.click_login_button(driver)

    # ==============================初始化密码==============================

    def new_password_input_value(self, driver, password_value):
        """在新密码输入框中输入内容

        Args:
            driver: WebDriver实例
            password_value: 要输入的新密码值

        Returns:
            元素操作结果
        """
        xpath = self.new_password_input()
        log.info(f"输入新密码：{password_value}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, password_value)

    def confirm_password_input_value(self, driver, password_value):
        """在确认密码输入框中输入内容

        Args:
            driver: WebDriver实例
            password_value: 要输入的确认密码值

        Returns:
            元素操作结果
        """
        xpath = self.confirm_password_input()
        log.info(f"输入确认密码：{password_value}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, password_value)

    def click_new_password_confirm_button(self, driver):
        """点击确认修改按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_password_confirm_button()
        log.info(f"点击确认修改按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def init_password(self, driver, new_password):
        """初始化密码操作

        Args:
            driver: WebDriver实例
            new_password: 新密码

        Returns:
            初始化密码操作结果
        """
        log.info(f"初始化密码：{new_password}")
        self.new_password_input_value(driver, new_password)
        self.confirm_password_input_value(driver, new_password)
        return self.click_new_password_confirm_button(driver)
