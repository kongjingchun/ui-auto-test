# encoding: utf-8
# @File  : OrderPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/17/16:59
# @Desc  :
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.OrderBase import OrderBase
from logs.log import log


class OrderPage(OrderBase, ObjectMap):
    def click_order_tab(self, driver, tab_name):
        log.info(f"奇幻订单tab到: {tab_name}")
        order_tab_xpath = self.order_tab(tab_name)
        return self.element_click(driver, By.XPATH, order_tab_xpath)

    def click_order_operate(self, driver, order_title, operate_name):
        log.info(f"商品名称: {order_title} ,执行 {operate_name} 操作")
        order_operate_xpath = self.order_operate(order_title, operate_name)
        return self.element_click(driver, By.XPATH, order_operate_xpath)

    def click_order_operate_confirm(self, driver):
        log.info("点击订单操作确认按钮")
        order_operate_confirm_xpath = self.order_operate_confirm()
        return self.element_click(driver, By.XPATH, order_operate_confirm_xpath)

    def click_logistics(self, driver):
        log.info("点击物流信息")
        return self.element_click(driver, By.XPATH, self.logistics())

    def click_logistics_select(self, driver, logistics_name):
        log.info("点击物流信息选择" + logistics_name)
        return self.element_click(driver, By.XPATH, self.logistics_select(logistics_name))

    def input_logistics_tracking_number(self, driver, tracking_number):
        log.info("输入物流单号" + tracking_number)
        return self.element_input_value(driver, By.XPATH, self.logistics_tracking_number(), tracking_number)

    def click_evaluation(self, driver, num):
        log.info("点击评价星:" + str(num))
        return self.element_click(driver, By.XPATH, self.evaluation(num))

    def click_submit_evaluation(self,driver):
        log.info("点击提交评价")
        return self.element_click(driver, By.XPATH, self.submit_evaluation())
