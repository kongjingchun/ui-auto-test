# encoding: utf-8
# @File  : MajorPortalManagePage.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 专业门户管理页面对象类，封装专业门户管理相关的页面操作方法

from time import sleep
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.ai_major.MajorPortalManageBase import MajorPortalManageBase
from logs.log import log


class MajorPortalManagePage(MajorPortalManageBase, ObjectMap):
    """专业门户管理页面类

    继承MajorPortalManageBase和ObjectMap类，提供专业门户管理页面元素操作方法
    """

    def switch_into_major_portal_manage_iframe(self, driver):
        """切换到专业门户管理iframe

        Args:
            driver: WebDriver实例

        Returns:
            切换操作结果
        """
        xpath = self.major_portal_manage_iframe()
        log.info(f"切换到专业门户管理iframe，xpath定位为：{xpath}")
        return self.switch_into_iframe(driver, By.XPATH, xpath)

    def switch_out_iframe(self, driver, to_root=False):
        """从iframe切出（通用方法）

        Args:
            driver: WebDriver实例
            to_root: True切回顶层文档，False切回上一层，默认为False

        Returns:
            切换操作结果
        """
        log.info("从iframe切出")
        return super().switch_out_iframe(driver, to_root=to_root)

    def input_search_keyword(self, driver, keyword):
        """输入搜索关键词

        Args:
            driver: WebDriver实例
            keyword: 搜索关键词

        Returns:
            输入操作结果
        """
        xpath = self.search_keyword_input()
        log.info(f"输入搜索关键词：{keyword}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, keyword)

    def click_search_button(self, driver):
        """点击搜索按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.search_button()
        log.info(f"点击搜索按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_open_portal_button_by_major_name(self, driver, major_name):
        """根据专业名称点击打开门户按钮

        Args:
            driver: WebDriver实例
            major_name: 专业名称

        Returns:
            点击操作结果
        """
        xpath = self.open_portal_button_by_major_name(major_name)
        log.info(f"根据专业名称'{major_name}'点击打开门户按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

    def click_edit_button_by_major_name(self, driver, major_name):
        """根据专业名称点击编辑按钮

        Args:
            driver: WebDriver实例
            major_name: 专业名称

        Returns:
            点击操作结果
        """
        xpath = self.edit_button_by_major_name(major_name)
        log.info(f"根据专业名称'{major_name}'点击编辑按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

    def click_tab_by_index(self, driver, index=1):
        """根据索引点击标签页

        Args:
            driver: WebDriver实例
            index: 标签页索引，从1开始，默认为1（第1个标签页）

        Returns:
            点击操作结果
        """
        xpath = self.tab_by_index(index)
        log.info(f"点击标签页（索引：{index}），xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_edit_page_button_by_major_name(self, driver, major_name):
        """根据专业名称点击编辑页面按钮

        Args:
            driver: WebDriver实例
            major_name: 专业名称
        """
        # 切换到专业门户管理iframe
        self.switch_into_major_portal_manage_iframe(driver)
        # 输入搜索关键词
        self.input_search_keyword(driver, major_name)
        # 点击搜索按钮
        self.click_search_button(driver)
        # 根据专业名称点击编辑按钮
        result = self.click_edit_button_by_major_name(driver, major_name)
        # 切出专业门户管理iframe
        self.switch_out_iframe(driver)
        log.info(f"根据专业名称'{major_name}'点击编辑按钮结果：{result}")
        return result

# ======================================= 编辑页面元素操作 ======================================

    def switch_into_major_portal_edit_iframe(self, driver):
        """切换到专业门户管理编辑页iframe

        Args:
            driver: WebDriver实例

        Returns:
            切换操作结果
        """
        xpath = self.major_portal_edit_iframe()
        log.info(f"切换到专业门户管理编辑页iframe，xpath定位为：{xpath}")
        return self.switch_into_iframe(driver, By.XPATH, xpath)

    def click_edit_page_button(self, driver):
        """点击编辑页面按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.edit_page_button()
        log.info(f"点击编辑页面按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_header_navigation_bar(self, driver):
        """点击头部导航栏

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.header_navigation_bar()
        log.info(f"点击头部导航栏，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def input_navigation_name(self, driver, navigation_name, index=1):
        """输入导航名称

        Args:
            driver: WebDriver实例
            navigation_name: 导航名称
            index: 导航索引，从1开始，默认为1（第1个导航）

        Returns:
            输入操作结果
        """
        xpath = self.navigation_name_input(index)
        log.info(f"输入导航名称（索引：{index}）：{navigation_name}，xpath定位为：{xpath}")
        self.element_click(driver, By.XPATH, xpath, timeout=10)
        result = self.element_input_value(driver, By.XPATH, xpath, navigation_name)
        return result

    def click_publish_button(self, driver):
        """点击发布按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.publish_button()
        log.info(f"点击发布按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_publish_confirm_button(self, driver):
        """点击发布确认按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.publish_confirm_button()
        log.info(f"点击发布确认按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_open_portal_link_in_edit_page(self, driver):
        """点击编辑页打开专业门户链接

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.open_portal_link_in_edit_page()
        log.info(f"点击编辑页打开专业门户链接，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)
    # 门户编辑

    def edit_portal(self, driver, navigation_name=None, index=1):
        """编辑门户

        Args:
            driver: WebDriver实例

        Returns:
            编辑操作结果
        """
        # 切换到专业门户管理编辑页iframe
        self.switch_into_major_portal_edit_iframe(driver)
        # 点击编辑页面按钮
        self.click_edit_page_button(driver)
        # 点击头部导航栏
        self.click_header_navigation_bar(driver)
        # 输入导航名称
        self.input_navigation_name(driver, navigation_name=navigation_name, index=1)
        # 点击发布按钮
        self.click_publish_button(driver)
        # 点击发布确认按钮
        self.click_publish_confirm_button(driver)
        # 点击编辑页打开专业门户链接
        self.click_open_portal_link_in_edit_page(driver)
        # 切出专业门户管理编辑页iframe
        self.switch_out_iframe(driver)
        # 切换到最新打开的窗口
        self.switch_to_new_window(driver)
        # 等待新页面加载完成
        self.wait_for_ready_state_complete(driver, timeout=10)
        sleep(1)  # 额外等待1秒，确保页面内容完全加载
        result = self.page_contains_text(driver, navigation_name)
        return result
