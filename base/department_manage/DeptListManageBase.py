# encoding: utf-8
# @File  : DeptListManageBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/29/16:24
# @Desc  : 院系列表管理

class DeptListManageBase:
    """院系列表管理页面元素定位基类"""

    def dept_manage_iframe(self):
        """院系管理iframe定位"""
        return "//iframe[@id='app-iframe-3004']"

    def new_dept_button(self):
        """新建院系按钮"""
        return "//button[contains(.,'新建院系')]"

    def new_dept_input(self, input_name):
        """
        新建院系输入框定位
        :param input_name: '代码' 或 '名称'
        """
        if '代码' in input_name:
            return "//input[contains(@placeholder,'请输入院系代码')]"
        elif '名称' in input_name:
            return "//input[contains(@placeholder,'请输入院系名称')]"
        else:
            return "//input[contains(@placeholder,'请输入院系代码')]"

    def new_dept_confirm_button(self):
        """新建确定按钮"""
        return "//span[text()='确定']/parent::button"

    def create_success_alert(self):
        """创建成功提示框"""
        return "//p[text()='创建成功']"

    def search_keyword_input(self):
        """搜索关键词输入框"""
        return "//input[@placeholder='院系名称 ｜ 院系代码']"

    def edit_button_hover_location(self, dept_code):
        """编辑悬停位置定位（根据院系代码）

        Args:
            dept_code: 院系代码
        """
        return "//tr[contains(.,'" + dept_code + "')]//i[contains(@class,'action-icon')]"

    def edit_button(self, dept_code):
        """编辑按钮定位（根据院系代码）

        Args:
            dept_code: 院系代码
        """
        return "//tr[contains(.,'" + dept_code + "')]//button"

    def delete_button(self):
        """删除院系按钮定位"""
        return "//button[contains(.,'删除院系')]"

    def delete_confirm_button(self):
        """删除确认按钮定位"""
        return "//div[contains(.,'警告')]//button[contains(.,'确定')]"

    def delete_success_alert(self):
        """删除成功提示框"""
        return "//p[contains(.,'删除成功')]"
