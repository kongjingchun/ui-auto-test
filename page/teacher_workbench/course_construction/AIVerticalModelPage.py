# encoding: utf-8
# @File  : AIVerticalModelPage.py
# @Author:
# @Date  :
# @Desc  : AI垂直模型页面对象类，封装AI垂直模型相关的页面操作方法
from selenium.webdriver.common.by import By

from base.BasePage import BasePage
from logs.log import log


class AIVerticalModelPage(BasePage):
    """AI垂直模型页面类

    继承BasePage类，提供AI垂直模型页面元素操作方法
    符合Selenium官方Page Object Model设计模式
    """

    def __init__(self, driver):
        """初始化AI垂直模型页面

        Args:
            driver: WebDriver实例
        """
        super().__init__(driver)

    # ==================== 元素定位器（静态定位器）====================
    # AI垂直模型iframe
    AI_VERTICAL_MODEL_IFRAME = (By.XPATH, "//iframe[@id='app-iframe-4002']")

    # ==================== 页面操作方法 ====================

    def switch_2_ai_vertical_model_iframe(self):
        """切换到AI垂直模型页面的iframe

        Returns:
            切换操作结果
        """
        log.info(f"切换到AI垂直模型页面的iframe，定位器为：{self.AI_VERTICAL_MODEL_IFRAME[1]}")
        return self.switch_to_iframe(self.AI_VERTICAL_MODEL_IFRAME)
