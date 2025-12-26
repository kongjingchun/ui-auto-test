# encoding: utf-8
# @File  : LeftMenuPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/25/12:05
# @Desc  : 左侧菜单页面类
from selenium.webdriver.common.by import By

from base.LeftMenuBase import LeftMenuBase
from base.ObjectMap import ObjectMap
from logs.log import log


class LeftMenuPage(LeftMenuBase, ObjectMap):
    """左侧菜单页面类"""
    
    def click_two_level_menu(self, driver, menu_name):
        """点击二级菜单"""
        log.info("点击二级菜单：" + menu_name)
        xpath = self.two_level_menu(menu_name)
        return self.element_click(driver, By.XPATH, xpath)
