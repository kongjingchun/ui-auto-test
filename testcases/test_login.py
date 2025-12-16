# encoding: utf-8
# @File  : test_login.py
# @Author: kongjingchun
# @Date  : 2025/12/01/18:37
# @Desc  :
from time import sleep

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage


class TestLogin:
    def test_login(self):
        driver = DriverConfig.driver_config()
        LoginPage().login(driver, "jay")
        sleep(5)
        driver.quit()
