# encoding: utf-8
# @File  : test_upload_personal_avatar.py
# @Author: kongjingchun
# @Date  : 2025/12/17/17:14
# @Desc  :
from time import sleep

from config.driver_config import DriverConfig
from page.AccountPage import AccountPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage


class TestPersonalInfo:
    def test_upload_personal_avatar(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, "账户设置")
        sleep(2)
        LeftMenuPage().click_level_two_menu(driver, "个人资料")
        sleep(2)
        AccountPage().upload_avatar(driver, "机器猫.jpg")
        sleep(2)
        AccountPage().click_save(driver)
        sleep(5)
        driver.quit()
