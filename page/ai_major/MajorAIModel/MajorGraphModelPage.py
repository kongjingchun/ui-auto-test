# encoding: utf-8
# @File  : MajorGraphModelPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 专业图谱模型页面对象类，封装专业图谱模型相关的页面操作方法

from inspect import isframe
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.ai_major.MajorAIModel.MajorGraphModelBase import MajorGraphModelBase
from logs.log import log


class MajorGraphModelPage(MajorGraphModelBase, ObjectMap):
    """专业图谱模型页面类

    继承MajorGraphModelBase和ObjectMap类，提供专业图谱模型页面的元素操作方法
    MajorGraphModelBase已继承MajorAIModelBase，可以访问父类的定位方法
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

    # ======================================= 专业图谱概览=========================================
    def click_create_major_graph_button(self, driver):
        """点击创建专业图谱按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.create_major_graph_button()
        log.info(f"点击创建专业图谱按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def input_create_major_graph_input(self, driver, graph_name):
        """输入创建图谱名称

        Args:
            driver: WebDriver实例
            graph_name: 图谱名称

        Returns:
            输入操作结果
        """
        xpath = self.create_major_graph_input()
        log.info(f"输入创建图谱名称：{graph_name}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, graph_name)

    def click_create_major_graph_confirm_button(self, driver):
        """点击创建图谱确认按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.create_major_graph_confirm_button()
        log.info(f"点击创建图谱确认按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_add_major_node_button(self, driver, node_type):
        """点击专业节点添加按钮（通用方法）

        Args:
            driver: WebDriver实例
            node_type: 节点类型，可选值：'能力'、'知识'、'素质'、'问题'

        Returns:
            点击操作结果
        """
        xpath = self.add_major_node_button(node_type)
        log.info(f"点击专业{node_type}节点添加按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def input_node_title_input(self, driver, node_title):
        """输入节点标题

        Args:
            driver: WebDriver实例
            node_title: 节点标题

        Returns:
            输入操作结果
        """
        xpath = self.node_title_input()
        log.info(f"输入节点标题：{node_title}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, node_title)

    def click_add_node_button(self, driver):
        """点击添加节点按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.add_node_button()
        log.info(f"点击添加节点按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def hover_node_by_name(self, driver, node_name):
        """悬浮到节点名称

        Args:
            driver: WebDriver实例
            node_name: 节点名称
        """
        xpath = self.node_by_name(node_name)
        log.info(f"悬浮到节点名称'{node_name}'，xpath定位为：{xpath}")
        return self.element_hover(driver, By.XPATH, xpath)

    def click_associate_node_button_by_name(self, driver, node_name):
        """根据节点名称点击关联按钮

        Args:
            driver: WebDriver实例
            node_name: 节点名称

        Returns:
            点击操作结果
        """
        xpath = self.associate_node_button_by_name(node_name)
        log.info(f"根据节点名称'{node_name}'点击关联按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_associate_node_category_by_name(self, driver, node_name):
        """根据节点名称点击关联分类

        Args:
            driver: WebDriver实例
            node_name: 节点名称

        Returns:
            点击操作结果
        """
        xpath = self.associate_node_category_by_name(node_name)
        log.info(f"根据节点名称'{node_name}'点击关联分类，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_checkbox_by_name(self, driver, node_name):
        """根据节点名称点击复选框

        Args:
            driver: WebDriver实例
            node_name: 节点名称

        Returns:
            点击操作结果
        """
        xpath = self.checkbox_by_name(node_name)
        log.info(f"根据节点名称'{node_name}'点击复选框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_associate_confirm_button(self, driver):
        """点击关联确定按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.associate_confirm_button()
        log.info(f"点击关联确定按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def create_major_graph_overview(self, driver):
        """创建专业图谱概览流程

        Args:
            driver: WebDriver实例

        Returns:
            创建操作结果
        """
        # 切换到专业AI模型iframe
        self.switch_into_major_ai_model_iframe(driver)
        # 点击创建专业图谱按钮
        self.click_create_major_graph_button(driver)
        # 输入图谱名称
        self.input_create_major_graph_input(driver, "测试图谱")
        # 点击创建确认按钮
        self.click_create_major_graph_confirm_button(driver)
        点击专业能力节点添加按钮
        self.click_add_major_node_button(driver, "能力")
        # 输入节点标题
        self.input_node_title_input(driver, "测试能力节点")
        # 点击添加节点按钮
        self.click_add_node_button(driver)
        # 点击专业知识节点添加按钮
        self.click_add_major_node_button(driver, "知识")
        # 输入节点标题
        self.input_node_title_input(driver, "测试知识节点")
        # 点击添加节点按钮
        self.click_add_node_button(driver)
        # 点击专业素质节点添加按钮
        self.click_add_major_node_button(driver, "素质")
        # 输入节点标题
        self.input_node_title_input(driver, "测试素质节点")
        # 点击添加节点按钮
        self.click_add_node_button(driver)
        # 点击专业问题节点添加按钮
        self.click_add_major_node_button(driver, "问题")
        # 输入节点标题
        self.input_node_title_input(driver, "测试问题节点")
        # 点击添加节点按钮
        self.click_add_node_button(driver)
        # 悬浮到测试能力节点
        self.hover_node_by_name(driver, "测试能力节点")
        # 点击测试能力节点关联按钮
        self.click_associate_node_button_by_name(driver, "测试能力节点")
        # 点击测试能力节点关联分类
        self.click_associate_node_category_by_name(driver, "知识")
        # 点击测试知识节点复选框
        self.click_checkbox_by_name(driver, "测试知识节点")
        # 点击测试知识节点关联确定按钮
        self.click_associate_confirm_button(driver)
        # 悬浮到测试素质节点
        self.hover_node_by_name(driver, "测试素质节点")
        # 点击测试素质节点关联按钮
        self.click_associate_node_button_by_name(driver, "测试素质节点")
        # 点击测试素质节点关联分类
        self.click_associate_node_category_by_name(driver, "问题")
        # 点击测试问题节点复选框
        self.click_checkbox_by_name(driver, "测试问题节点")
        # 点击测试问题节点关联确定按钮
        result = self.click_associate_confirm_button(driver)
        # 切出专业AI模型iframe
        self.switch_out_iframe(driver)
        return result
