# encoding: utf-8
# @File  : CourseManageBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 课程管理页面元素定位基类

class CourseManageBase:
    """课程管理页面元素定位基类

    提供课程管理相关页面元素的XPath定位表达式
    """

    def course_manage_iframe(self):
        """课程管理iframe定位"""
        return "//iframe[@id='app-iframe-2001']"

    def new_course_button(self):
        """新建课程按钮"""
        return "//button[contains(.,'新建课程')]"

    def new_course_input(self, input_name):
        """新建课程输入框定位

        Args:
            input_name: 输入框名称，如 '名称'、'代码'、'描述'
        """

        if '代码' in input_name:
            return "//div[@aria-label='新建课程'] //input[contains(@placeholder,'课程代码')]"
        elif '名称' in input_name:
            return "//div[@aria-label='新建课程'] //input[contains(@placeholder,'课程名称')]"
        elif '描述' in input_name:
            return "//div[@aria-label='新建课程'] //textarea[contains(@placeholder,'课程描述')]"
        else:
            return None

    def new_course_dept_dropdown(self):
        """所属学院下拉框"""
        return "//div[@aria-label='新建课程']//span[text()='请选择学院']/parent::div"

    def new_course_dept_dropdown_option(self, dept_name):
        """所属学院下拉框选项"""
        return "//div[@aria-hidden='false']//span[contains(.,'auto_dept11')]/parent::li"

    def new_course_responsible_person_dropdown(self):
        """课程负责人下拉框"""
        return "//div[@aria-label='新建课程']//span[text()='请选择课程负责人']/parent::div"

    def new_course_responsible_person_dropdown_option(self, prof_name):
        """课程负责人下拉框选项"""
        return "//div[@aria-hidden='false']//span[text()='" + prof_name + "']/parent::li | //div[@x-placement]//span[text()='" + prof_name + "']/parent::li"

    def new_course_first_class_switch(self):
        """是否一流课程开关"""
        return "//div[@aria-label='新建课程']//span[contains(text(),'是否一流课程')]/following-sibling::span//span[contains(@class,'el-switch__core')] | //div[@aria-label='新建课程']//label[contains(text(),'是否一流课程')]/following-sibling::div//span[contains(@class,'el-switch__core')]"

    def new_course_confirm_button(self):
        """新建确定按钮"""
        return "//div[@aria-label='新建课程']//span[contains(.,'确定')]/parent::button | //div[@aria-label='新建课程']//button[contains(.,'确定')]"

    def create_success_alert(self):
        """创建成功提示框"""
        return "//p[@class='el-message__content' and text()='新建成功'] | //p[text()='新建成功'] | //p[contains(text(),'创建成功')]"
