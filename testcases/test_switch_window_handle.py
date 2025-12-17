# encoding: utf-8
# @File  : test_switch_window_handle.py
# @Author: kongjingchun
# @Date  : 2025/12/17/16:16
# @Desc  :
from time import sleep

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage

class TestSwitchWindowHandle:
    def test_switch_window_handle(self):
        driver = DriverConfig.driver_config()
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "外链")
        sleep(5)
        title = ExternalLinkPage().goto_imooc(driver)
        print("网址切换到"+title)
        sleep(5)
        driver.quit()
