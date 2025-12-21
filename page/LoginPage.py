# encoding: utf-8
# @File  : LoginPage.py
# @Author: kongjingchun
# @Date  : 2025/12/01/18:31
# @Desc  :

from selenium.webdriver.common.by import By
from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf


class LoginPage(LoginBase, ObjectMap):
    def login_input_value(self, driver, input_placeholder, input_value):
        """
        在登录页面的输入框中填入指定值

        :param driver: WebDriver实例
        :param input_placeholder: 输入框的placeholder属性值
        :param input_value: 要输入的值
        :return: None
        """
        input_xpath = LoginBase.login_input(input_placeholder)  # 调用父类方法
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def click_login(self, driver, button_name):
        """
        点击登录页面的按钮

        :param driver: WebDriver实例
        :param button_name: 按钮显示文本
        :return: None
        """
        button_xpath = LoginBase.login_button(button_name)  # 调用父类方法
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver, user):
        self.element_to_url(driver, "/login")
        username, password = GetConf().get_username_password(user)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        self.click_login(driver, "登录")
        self.assert_login(driver)

    def assert_login(self, driver):
        login_success_xpath = LoginBase.login_successful()
        return self.element_appear(driver, By.XPATH, login_success_xpath, timeout=2)

    def login_assert(self, driver, img_name):
        assert self.find_img_in_source(driver, img_name) > 0.9, "未找到合适的图片"
