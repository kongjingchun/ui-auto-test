# encoding: utf-8
# @File  : HomePage.py
# @Author: kongjingchun
# @Date  : 2025/12/23/13:36
# @Desc  :
from selenium.webdriver.common.by import By

from base.HomeBase import HomeBase
from base.ObjectMap import ObjectMap


class HomePage(HomeBase, ObjectMap):
    def get_user_balance(self, driver):
        """
        获取用户余额
        :param driver:
        :return:
        """
        balance_xpath = HomeBase.user_balance()
        return self.element_get(driver, By.XPATH, balance_xpath).text
