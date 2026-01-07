# encoding: utf-8
# @File  : MajorGraphModelBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 专业图谱模型页面元素定位基类

from base.ai_major.MajorAIModel.MajorAIModelBase import MajorAIModelBase


class MajorGraphModelBase(MajorAIModelBase):
    """专业图谱模型页面元素定位基类

    提供专业图谱模型相关页面元素的XPath定位表达式
    """

# ======================================= 专业图谱概览=========================================
    def create_major_graph_button(self):
        """创建专业图谱按钮"""
        return "//button[./span[contains(.,'创建专业图谱')]]"

    def create_major_graph_input(self):
        """创建图谱名称输入框"""
        return "//input[@placeholder='请输入图谱名称']"

    def create_major_graph_confirm_button(self):
        """创建图谱创建按钮"""
        return "//div[@aria-label='创建专业图谱']//button[./span[contains(.,'创建')]]"

    def add_major_node_button(self, node_type):
        """专业节点添加按钮（通用方法）

        Args:
            node_type: 节点类型，可选值：'能力'、'知识'、'素质'、'问题'

        Returns:
            节点添加按钮的XPath定位表达式
        """
        if '能力' in node_type:
            return "//h4[text()='专业能力节点']/following-sibling::div/button"
        elif '知识' in node_type:
            return "//h4[text()='专业知识节点']/following-sibling::div/button"
        elif '素质' in node_type:
            return "//h4[text()='专业素质节点']/following-sibling::div/button"
        elif '问题' in node_type:
            return "//h4[text()='专业问题节点']/following-sibling::div/button"

    def node_title_input(self):
        """节点标题输入框"""
        return "//div[@aria-label='添加节点']//input[contains(@placeholder,'节点标题')]"

    def add_node_button(self):
        """添加节点按钮"""
        return "//div[@aria-label='添加节点']//button[contains(.,'添加')]"

    def node_by_name(self, node_name):
        """根据节点名称定位节点"""
        return "//div[text()='" + node_name + "']"

    def associate_node_button_by_name(self, node_name):
        """根据节点名称定位关联按钮"""
        return "//div[contains(@class,'node-list') and contains(.,'" + node_name + "')]//button[2]"

    def associate_node_category_by_name(self, node_name):
        """根据节点名称定位关联分类"""
        if '能力' in node_name:
            return "//span[text()='专业能力节点']//parent::button"
        elif '知识' in node_name:
            return "//span[text()='专业知识节点']//parent::button"
        elif '素质' in node_name:
            return "//span[text()='专业素质节点']//parent::button"
        elif '问题' in node_name:
            return "//span[text()='专业问题节点']//parent::button"

    def checkbox_by_name(self, node_name):
        """根据节点名称定位复选框"""
        return "//label[contains(.,'" + node_name + "')]/span[1]"

    def associate_confirm_button(self):
        """关联确定按钮"""
        return "//button[contains(.,'确定')]"
