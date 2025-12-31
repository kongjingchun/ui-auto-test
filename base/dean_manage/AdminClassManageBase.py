# encoding: utf-8
# @File  : AdminClassManageBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 行政班管理页面元素定位基类

class AdminClassManageBase:
    """行政班管理页面元素定位基类

    提供行政班管理相关页面元素的XPath定位表达式
    """

    def admin_class_manage_iframe(self):
        """行政班管理iframe定位"""
        return "//iframe[@id='app-iframe-2005']"

    def new_admin_class_button(self):
        """新建行政班按钮"""
        return "//button[contains(.,'新建行政班')]"

    def new_admin_class_input(self, input_name):
        """新建行政班输入框定位

        Args:
            input_name: 输入框名称，如 '名称'、'编号'、'描述'
        """
        if '名称' in input_name:
            return "//input[contains(@placeholder,'请输入行政班名称')]"
        elif '编号' in input_name:
            return "//input[contains(@placeholder,'请输入行政班编号')]"
        elif '描述' in input_name:
            return "//textarea[contains(@placeholder,'请输入行政班描述')]"
        else:
            return "//input[contains(@placeholder,'请输入行政班名称')]"

    def new_admin_class_dept_dropdown(self):
        """所属学院下拉框"""
        return "//div[contains(@aria-label,'新建行政班')]//span[text()='请选择学院']/parent::div"

    def new_admin_class_dept_dropdown_option(self, dept_name):
        """所属学院下拉框选项"""
        return "//div[@aria-hidden='false']//span[text()='" + dept_name + "']/parent::li"

    def new_admin_class_major_dropdown(self):
        """所属专业下拉框"""
        return "//span[text()='请先选择学院']/parent::div"

    def new_admin_class_major_dropdown_option(self, major_name):
        """所属专业下拉框选项"""
        return "//div[@aria-hidden='false']//span[text()='" + major_name + "']/parent::li"

    def new_admin_class_grade_dropdown(self):
        """年级下拉框"""
        return "//div[contains(@aria-label,'新建行政班')]//span[text()='请选择年级']/parent::div"

    def new_admin_class_grade_dropdown_option(self, grade):
        """年级下拉框选项"""
        return "//div[@aria-hidden='false']//span[text()='" + grade + "']/parent::li"

    def new_admin_class_confirm_button(self):
        """新建确定按钮"""
        return "//div[contains(@aria-label,'新建行政班')]//span[contains(.,'创建')]/parent::button"

    def create_success_alert(self):
        """创建成功提示框"""
        return "//p[@class='el-message__content' and text()='创建成功']"
