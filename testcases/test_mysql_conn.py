# encoding: utf-8
# @File  : test_mysql_conn.py
# @Author: kongjingchun
# @Date  : 2025/12/23/13:38
# @Desc  :
import allure

from common.mysql_operate import MysqlOperate
from common.report_add_img import add_img_2_report
from logs.log import log
from page.HomePage import HomePage
from page.LoginPage import LoginPage


class TestMysqlConn:
    @allure.feature("获取账户余额与数据库对比")
    @allure.description("获取账户余额与数据库对比")
    def test_mysql_conn(self, driver):
        with allure.step("登录"):
            LoginPage().login(driver, "jay")
            add_img_2_report(driver, '登录')
        with allure.step("获取账户余额"):
            balance = HomePage().get_user_balance(driver)
            log.info(f"账户余额为：{balance}")
            add_img_2_report(driver, '获取账户余额')
        with allure.step("获取数据库余额"):
            db_balance = MysqlOperate().query("select balance from wallet where user_id=13;")
            log.info(f"数据库余额为：{db_balance[0][0]}")
        with allure.step("断言"):
            assert balance == str(db_balance[0][0])
