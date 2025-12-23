# encoding: utf-8
# @File  : LeftMenuPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/16/16:13
# @Desc  : 左侧菜单页面操作类，用于点击一级和二级菜单项

from selenium.webdriver.common.by import By

from base.LeftMenuBase import LeftMenuBase
from base.ObjectMap import ObjectMap


class LeftMenuPage(LeftMenuBase, ObjectMap):
    """
    左侧菜单页面操作类
    继承自 LeftMenuBase 和 ObjectMap，提供菜单点击功能
    """

    def click_level_one_menu(self, driver, menu_name):
        """
        点击一级菜单

        Args:
            driver: 浏览器驱动对象
            menu_name: 菜单名称

        Returns:
            点击操作的结果
        """
        xpath = self.level_one_menu(menu_name)
        return self.element_click(driver, By.XPATH, xpath)

    def click_level_two_menu(self, driver, menu_name):
        """
        点击二级菜单

        Args:
            driver: 浏览器驱动对象
            menu_name: 菜单名称

        Returns:
            点击操作的结果
        """
        xpath = self.level_two_menu(menu_name)
        return self.element_click(driver, By.XPATH, xpath)
