# encoding: utf-8
# @File  : GoodsPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/17/11:43
# @Desc  :

from base.IframeBaiduMapBase import IframeBaiduMapBase
from base.ObjectMap import ObjectMap
from selenium.webdriver.common.by import By


class IframeBaiduMapPage(IframeBaiduMapBase, ObjectMap):

    def input_baidu_map_search(self, driver, search_value):
        """
        获取百度地图输入框输入内容
        :param driver:
        :param search_value:
        :return:
        """
        input_xpath = self.search_input()
        return self.element_fill_value(driver, By.XPATH, input_xpath, search_value)

    def click_baidu_map_search_button(self, driver):
        """
        点击百度地图搜索按钮
        :param driver:
        :return:
        """
        button_xpath = self.search_button()
        return self.element_click(driver, By.XPATH, button_xpath)

    def switch_2_baidu_map_iframe(self, driver):
        """
        切换到百度地图iframe
        :param driver:
        :return:
        """
        iframe_xpath = self.baidu_map_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def iframe_out(self, driver):
        """
        iframe退出
        :param driver:
        :return:
        """
        return self.switch_from_iframe_to_content(driver)
