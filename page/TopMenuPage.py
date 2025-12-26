# encoding: utf-8
# @File  : TopMenuPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/25/11:03
# @Desc  :
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.TopMenuBase import TopMenuBase
from logs.log import log


class TopMenuPage(TopMenuBase, ObjectMap):

    def click_school_switch(self, driver):
        """
        点击学校切换按钮
        :param driver:
        :return:
        """
        log.info("点击学校切换按钮")
        xpath = self.school_switch()
        return self.element_click(driver, By.XPATH, xpath)

    def click_school_switch_list(self, driver, school_name):
        """
        选择切换的学校
        :param driver:
        :param school_name:
        :return:
        """
        log.info("选择切换为" + school_name + "学校")
        xpath = self.school_switch_list(school_name)
        return self.element_click(driver, By.XPATH, xpath)

    def click_role_switch(self, driver):
        """
        点击角色切换按钮
        :param driver:
        :return:
        """
        log.info("点击角色切换按钮")
        xpath = self.role_switch()
        return self.element_click(driver, By.XPATH, xpath)

    def click_role_switch_list(self, driver, role_name):
        """
        选择切换的角色
        :param driver:
        :param role_name:
        :return:
        """
        log.info("选择切换为 [" + role_name + "] 角色")
        xpath = self.role_switch_list(role_name)
        return self.element_click(driver, By.XPATH, xpath)

    # 切换学校
    def switch_school(self, driver, school_name):
        """切换学校"""
        self.click_school_switch(driver)
        self.click_school_switch_list(driver, school_name)

    def switch_role(self, driver, role_name):
        """切换角色"""
        self.click_role_switch(driver)
        self.click_role_switch_list(driver, role_name)
