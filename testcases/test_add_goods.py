# encoding: utf-8
# @File  : test_add_goods.py
# @Author: kongjingchun
# @Date  : 2025/12/17/14:27
# @Desc  :
from time import sleep

from config.driver_config import DriverConfig
from page.GoodsPage import GoodsPage
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage


class TestAddGoods:
    def test_add_goods_001(self):
        driver = DriverConfig.driver_config()
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver,"新增二手商品" )
        sleep(2)
        GoodsPage().add_new_goods(driver, "测试商品", "商品详情", 10, ["机器猫.jpg"], 66, "上架", "提交")
        sleep(5)
