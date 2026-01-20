# encoding: utf-8
# @File  : login_page.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/21:17
# @Desc  : 登录页面对象类，封装登录相关的页面操作方法

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from logs.log import log


class LoginPage(BasePage):
    """登录页面类

    继承BasePage类，提供登录页面的元素操作方法
    符合Selenium官方Page Object Model设计模式
    """

    def __init__(self, driver):
        """初始化登录页面

        Args:
            driver: WebDriver实例
        """
        super().__init__(driver)

    # ==================== 定位器 ====================

    # 登录的首页按钮
    login_page_first_loc = (By.XPATH, "//button[span[text()='登录']]")
    # 切换登录方式
    login_method_loc = (By.XPATH, "//div[contains(@class,'login-switch')]")
    # 账号登录输入框
    login_account_loc = (By.XPATH, "//div[contains(@class, 'text el-input')]//input[@placeholder='请输入账号']")
    # 密码输入框
    password_loc = (By.XPATH, "//div[contains(@class, 'text el-input el-input--suffix')]//input[@placeholder='请输入密码']")
    # 记住密码复选框
    remember_loc = (By.XPATH, "//label[@class='el-checkbox']")
    # 登录按钮
    login_btn_loc = (By.XPATH, "//button[span[text()='登 录']]")
    # 我的资源元素
    my_resource = (By.ID, 'my_resource')

    # ==================== 页面操作方法 ====================

    def login_first(self, username="20210708", password="Abcd1234"):
        """执行登录操作

        Args:
            username: 用户名，默认"20210708"
            password: 密码，默认"Abcd1234"

        Returns:
            bool: 登录操作结果，True表示成功
        """
        log.info(f"执行登录操作，用户名：{username}")
        try:
            self.navigate_to("/pro/portal/home/")
            self.click(self.login_page_first_loc)
            self.click(self.login_method_loc)
            self.input_text(self.login_account_loc, username)
            self.input_text(self.password_loc, password)
            self.click(self.remember_loc)
            self.click(self.login_btn_loc)
            self.jy_slide()
            return True
        except Exception as e:
            log.error(f"登录操作失败：{str(e)}")
            return False
