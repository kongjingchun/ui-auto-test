# encoding: utf-8
# @File  : OrderPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/17/16:59
# @Desc  :
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.OrderBase import OrderBase


class OrderPage(OrderBase, ObjectMap):
    def click_order_tab(self, driver, tab_name):
        order_tab_xpath = self.order_tab(tab_name)
        return self.element_click(driver, By.XPATH, order_tab_xpath)
