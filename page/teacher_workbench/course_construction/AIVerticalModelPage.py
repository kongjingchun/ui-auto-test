# encoding: utf-8
# @File  : AIVerticalModelPage.py
# @Author:
# @Date  :
# @Desc  : AI垂直模型页面对象类，封装AI垂直模型相关的页面操作方法

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.teacher_workbench.course_construction.AIVerticalModelBase import AIVerticalModelBase
from logs.log import log


class AIVerticalModelPage(AIVerticalModelBase, ObjectMap):
    """AI垂直模型页面类

    继承AIVerticalModelBase和ObjectMap类，提供AI垂直模型页面的元素操作方法
    """

    def switch_into_ai_vertical_model_iframe(self, driver):
        """切换到AI垂直模型iframe

        Args:
            driver: WebDriver实例

        Returns:
            切换操作结果
        """
        xpath = self.ai_vertical_model_iframe()
        log.info(f"切换到AI垂直模型iframe，xpath定位为：{xpath}")
        return self.switch_into_iframe(driver, By.XPATH, xpath)

    # # 左侧菜单栏
    # def click_left_menu_by_name(self, driver, menu_name):
    #     """根据菜单名称点击左侧菜单栏

    #     Args:
    #         driver: WebDriver实例
    #         menu_name: 菜单名称

    #     Returns:
    #         点击操作结果
    #     """
    #     xpath = self.left_menu_by_name(menu_name)
    #     log.info(f"点击左侧菜单栏：{menu_name}，xpath定位为：{xpath}")
