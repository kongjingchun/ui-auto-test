# encoding: utf-8
# @File  : LoginPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/01/18:31
# @Desc  :
import time
from time import sleep

import requests
from selenium.webdriver.common.by import By
from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.ocr_identify import OCRIdentify
from common.report_add_img import add_img_path_2_report
from common.yaml_config import GetConf
from logs.log import log


class LoginPage(LoginBase, ObjectMap):
    def login_input_value(self, driver, input_placeholder, input_value):
        """
        在登录页面的输入框中填入指定值

        :param driver: WebDriver实例
        :param input_placeholder: 输入框的placeholder属性值
        :param input_value: 要输入的值
        :return: None
        """
        log.info("输入" + input_placeholder + "为：" + str(input_value))
        input_xpath = LoginBase.login_input(input_placeholder)  # 调用父类方法
        return self.element_input_value(driver, By.XPATH, input_xpath, input_value)

    def click_login(self, driver, button_name):
        """
        点击登录页面的按钮

        :param driver: WebDriver实例
        :param button_name: 按钮显示文本
        :return: None
        """
        log.info("点击登录")
        button_xpath = LoginBase.login_button(button_name)  # 调用父类方法
        return self.element_click(driver, By.XPATH, button_xpath)

    def click_need_captcha(self, driver):
        need_captcha_xpath = LoginBase.need_captcha()
        return self.element_click(driver, By.XPATH, need_captcha_xpath)

    def login(self, driver, user, need_xpath=False):
        self.element_to_url(driver, "/login")
        if need_xpath:
            log.info("需要验证码")
            self.click_need_captcha(driver)
            captcha_xpath = self.captcha()
            captcha_path = self.element_screenshot(driver, By.XPATH, captcha_xpath)
            add_img_path_2_report(captcha_path, "图像验证码")
            ocr_value = OCRIdentify().identify(captcha_path)
            log.info("验证码识别结果为：" + ocr_value)
            self.login_input_value(driver, "请输入验证码", ocr_value)
            sleep(1)
        username, password = GetConf().get_username_password(user)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        self.click_need_captcha(driver)
        self.click_login(driver, "登录")
        self.assert_login(driver)

    def api_login(self, driver, user):
        log.info('跳转登录')
        self.element_to_url(driver, "/login")
        username, password = GetConf().get_username_password(user)
        url = GetConf().get_url()
        data = {
            "user": username,
            "password": password
        }
        log.info('通过api登录')
        res = requests.post(url + "/api/user/login", json=data)
        token = res.json()["data"]["token"]
        js_script = "window.sessionStorage.setItem('token','%s');" % token
        driver.execute_script(js_script)
        time.sleep(2)
        self.element_to_url(driver, "/")

    def assert_login(self, driver):
        login_success_xpath = LoginBase.login_successful()
        return self.element_appear(driver, By.XPATH, login_success_xpath, timeout=2)

    def login_assert(self, driver, img_name):
        """
        登录后进行图像断言
        :param driver: 浏览器驱动
        :param img_name: 要匹配的图像名称
        :return: 返回匹配置信度值
        """
        confidence = self.find_img_in_source(driver, img_name)
        return confidence
