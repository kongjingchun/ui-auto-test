# encoding: utf-8
# @File  : DepListManageBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/29/16:24
# @Desc  : 院系列表管理

class DepListManageBase:
    """院系列表管理页面元素定位基类"""

    def dep_manage_iframe(self):
        """院系管理iframe定位"""
        return "//iframe[@id='app-iframe-3004']"

    def new_dep_button(self):
        """新建院系按钮"""
        return "//button[contains(.,'新建院系')]"

    def new_dep_input(self, input_name):
        """
        院系输入框定位
        :param input_name: '代码' 或 '名称'
        """
        if '代码' in input_name:
            return "//input[contains(@placeholder,'请输入院系代码')]"
        elif '名称' in input_name:
            return "//input[contains(@placeholder,'请输入院系名称')]"
        else:
            return "//input[contains(@placeholder,'请输入院系代码')]"

    def new_dep_confirm_button(self):
        """新建确定按钮"""
        return "//span[text()='确定']/parent::button"

    def create_success_alert(self):
        """创建成功提示框"""
        return "//p[text()='创建成功']"