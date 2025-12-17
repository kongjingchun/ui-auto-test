# encoding: utf-8
# @File  : GoodsPage.py
# @Author: kongjingchun
# @Date  : 2025/12/17/11:43
# @Desc  :
from time import sleep

from selenium.webdriver.common.by import By

from base.GoodsBase import GoodsBase
from base.ObjectMap import ObjectMap
from common.tools import get_img_path


class GoodsPage(GoodsBase, ObjectMap):

    def input_goods_title(self, driver, input_value):
        good_title_xpath = self.goods_title()
        return self.element_fill_value(driver, By.XPATH, good_title_xpath, input_value)

    def input_goods_details(self, driver, input_value):
        good_details_xpath = self.goods_details()
        return self.element_fill_value(driver, By.XPATH, good_details_xpath, input_value)

    def select_goods_num(self, driver, num):
        good_num_xpath = self.goods_num(True)
        for i in range(num):
            self.element_click(driver, By.XPATH, good_num_xpath)
            sleep(0.5)

    def upload_goods_img(self, driver, img_path):
        file_path = get_img_path(img_path)
        goods_img_xpath = self.goods_img()
        return self.upload(driver, By.XPATH, goods_img_xpath, file_path)

    def input_goods_price(self, driver, input_value):
        good_price_xpath = self.goods_price()
        return self.element_fill_value(driver, By.XPATH, good_price_xpath, input_value)

    def select_goods_status(self, driver, select_name):
        good_status_xpath = self.goods_status()
        self.element_click(driver, By.XPATH, good_status_xpath)
        good_status_select_xpath = self.goods_status_select(select_name)
        return self.element_click(driver, By.XPATH, good_status_select_xpath, select_name)

    def click_bottom_button(self, driver, button_name):
        button_xpath = self.add_goods_bottom_button(button_name)
        return self.element_click(driver, By.XPATH, button_xpath)

    def add_new_goods(self, driver, title, details, num, img_list, price, status, bottom_button_name):
        self.input_goods_title(driver, title)
        self.input_goods_details(driver, details)
        self.select_goods_num(driver, num)
        for img_path in img_list:
            self.upload_goods_img(driver, img_path)
            sleep(5)
        self.input_goods_price(driver, price)
        self.select_goods_status(driver, status)
        self.click_bottom_button(driver, bottom_button_name)
        return True
