# encoding: utf-8
# @File  : LoginPage.py
# @Author: kongjingchun
# @Date  : 2025/12/01/18:31
# @Desc  :

from selenium.webdriver.common.by import By
from base.LoginBase import LoginBase


class LoginPage(LoginBase):
    def login_input_value(self, driver, input_placeholder, input_value):
        """
        登录页输入
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        input_xpath = LoginBase.login_input(input_placeholder)  # 修正调用父类方法
        return driver.find_element(By.XPATH, input_xpath).send_keys(input_value)

    def click_login(self, driver, button_name):
        """
        登录按钮
        :param driver:
        :param button_name:
        :return:
        """
        button_xpath = LoginBase.login_button(button_name)  # 修正调用父类方法
        return driver.find_element(By.XPATH, button_xpath).click()
