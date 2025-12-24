# encoding: utf-8
# @File  : test_trading_flow.py
# @Author: 孔敬淳
# @Date  : 2025/12/23/14:45
# @Desc  :
from time import sleep

import allure
import pytest

from common.report_add_img import add_img_2_report
from common.tools import get_now_time_str
from page.GoodsPage import GoodsPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.OrderPage import OrderPage
from page.TradingMarketPage import TradingMarketPage


class TestTradingFlow:
    @pytest.mark.trading_flow
    @allure.feature("交易流程")
    @allure.description("测试交易流程")
    def test_trading_flow(self, driver):
        with allure.step("登录卖家"):
            LoginPage().api_login(driver, "kshoujia")
            add_img_2_report(driver, "登录卖家")
        with allure.step("进入新增商品页"):
            LeftMenuPage().click_level_one_menu(driver, "产品")
            LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
            add_img_2_report(driver, "进入新增商品页")
            title = "测试商品" + get_now_time_str()
        with allure.step("新增二手商品"):
            GoodsPage().add_new_goods(
                driver=driver,
                title=title,
                details="测试商品详情" + get_now_time_str(),
                num=3,
                img_list=["机器猫.jpg"],
                price=10,
                status="上架",
                bottom_button_name="提交"

            )
            add_img_2_report(driver, "新增二手商品")
            sleep(3)

        with allure.step("登录买家"):
            LoginPage().api_login(driver, "kmaijia")
            add_img_2_report(driver, "登录买家")
        with allure.step("进入交易市场"):
            LeftMenuPage().click_level_one_menu(driver, "交易市场")
            add_img_2_report(driver, "进入交易市场")
        with allure.step("搜索商品"):
            TradingMarketPage().input_search_input(driver, title)
            TradingMarketPage().click_search_button(driver)
            add_img_2_report(driver, "搜索商品")
        with allure.step("点击商品卡片"):
            TradingMarketPage().click_product_card(driver, title)
            add_img_2_report(driver, "点击商品卡片")
        with allure.step("点击我想要"):
            TradingMarketPage().click_i_want(driver)
            add_img_2_report(driver, "点击我想要")
        with allure.step("填写购买信息"):
            TradingMarketPage().input_buy_number(driver, 1)
            TradingMarketPage().click_address(driver)
            TradingMarketPage().click_address_detail(driver)
            add_img_2_report(driver, "填写购买信息")
        with allure.step("点击确认"):
            TradingMarketPage().click_confirm_button(driver)
            add_img_2_report(driver, "点击确认")
        with allure.step("买家支付"):
            OrderPage().click_order_operate(driver, title, "去支付")
            OrderPage().click_order_operate_confirm(driver)
            add_img_2_report(driver, "买家支付成功")
        with allure.step("登录卖家"):
            LoginPage().api_login(driver, "kshoujia")
            add_img_2_report(driver, "登录卖家")
        with allure.step("进入已卖出的宝贝"):
            LeftMenuPage().click_level_one_menu(driver, "我的订单")
            LeftMenuPage().click_level_two_menu(driver, "已卖出的宝贝")
            add_img_2_report(driver, "进入已卖出的宝贝")
        with allure.step("卖家发货"):
            OrderPage().click_order_tab(driver, "待发货")
            OrderPage().click_order_operate(driver, title, "去发货")
            OrderPage().click_logistics(driver)
            OrderPage().click_logistics_select(driver, "顺丰速运")
            OrderPage().input_logistics_tracking_number(driver, "111111111111")
            OrderPage().click_order_operate_confirm(driver)
            add_img_2_report(driver, "卖家发货成功")
        with allure.step("登录买家"):
            LoginPage().api_login(driver, "kmaijia")
            add_img_2_report(driver, "登录买家")
        with allure.step("进入已买到的宝贝"):
            LeftMenuPage().click_level_one_menu(driver, "我的订单")
            LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
            add_img_2_report(driver, "进入已买到的宝贝")
        with allure.step("确认收货"):
            OrderPage().click_order_tab(driver, "待确认")
            OrderPage().click_order_operate(driver, title, "去确认收货")
            OrderPage().click_order_operate_confirm(driver)
            add_img_2_report(driver, "确认收货成功")
        with allure.step("评价"):
            OrderPage().click_order_tab(driver, "待评价")
            OrderPage().click_order_operate(driver, title, "去评价")
            OrderPage().click_evaluation(driver, 5)
            OrderPage().click_submit_evaluation(driver)
            add_img_2_report(driver, "评价成功")
            sleep(5)
