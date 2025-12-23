# encoding: utf-8
# @File  : TestOrderBuy.py
# @Author: 孔敬淳
# @Date  : 2025/12/17/17:01
# @Desc  :
from time import sleep

import pytest

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.OrderPage import OrderPage

tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]


class TestOrderBuy:
    @pytest.mark.parametrize("tab_name", tab_list)
    def test_order_buy(self, driver, tab_name):
        LoginPage().login(driver, "jay")
        sleep(1)
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        sleep(1)
        tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]
        OrderPage().click_order_tab(driver, tab_name)
        sleep(1)
