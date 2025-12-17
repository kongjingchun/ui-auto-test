# encoding: utf-8
# @File  : TestOrderBuy.py
# @Author: kongjingchun
# @Date  : 2025/12/17/17:01
# @Desc  :
from time import sleep

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.OrderPage import OrderPage


class TestOrderBuy:
    driver = DriverConfig.driver_config()
    LoginPage().login(driver, "jay")
    sleep(1)
    LeftMenuPage().click_level_one_menu(driver, "我的订单")
    sleep(1)
    LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
    sleep(1)
    OrderPage().click_order_tab(driver, "全部")
    sleep(1)
    OrderPage().click_order_tab(driver, "待付款")
    sleep(1)
    OrderPage().click_order_tab(driver, "待发货")
    sleep(1)
    OrderPage().click_order_tab(driver, "运输中")
    sleep(1)
    OrderPage().click_order_tab(driver, "待确认")
    sleep(1)
    OrderPage().click_order_tab(driver, "待评价")
    sleep(5)
    driver.quit()