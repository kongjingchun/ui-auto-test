# encoding: utf-8
# @File  : MajorAIModelPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 专业AI模型页面对象类，封装专业AI模型相关的页面操作方法

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.ai_major.MajorAIModel.MajorAIModelBase import MajorAIModelBase
from logs.log import log


class MajorAIModelPage(MajorAIModelBase, ObjectMap):
    """专业AI模型页面类

    继承MajorAIModelBase和ObjectMap类，提供专业AI模型页面的元素操作方法
    """

    def switch_into_major_ai_model_iframe(self, driver):
        """切换到专业AI模型iframe

        Args:
            driver: WebDriver实例

        Returns:
            切换操作结果
        """
        xpath = self.major_ai_model_iframe()
        log.info(f"切换到专业AI模型iframe，xpath定位为：{xpath}")
        return self.switch_into_iframe(driver, By.XPATH, xpath)

    def click_menu_by_name(self, driver, menu_name):
        """根据菜单名称点击菜单

        Args:
            driver: WebDriver实例
            menu_name: 菜单名称

        Returns:
            点击操作结果
        """
        # 切换到专业AI模型iframe
        self.switch_into_major_ai_model_iframe(driver)
        # 根据菜单名称点击菜单
        xpath = self.menu_by_name(menu_name)
        log.info(f"点击菜单：{menu_name}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath)
        # 切出专业AI模型iframe
        self.switch_out_iframe(driver)
        return result
