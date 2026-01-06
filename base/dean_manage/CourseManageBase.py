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

    def search_keyword_input(self):
        """搜索关键词输入框"""
        return "//input[@placeholder='课程代码 ｜ 课程名称']"

    def edit_button_hover_location(self, course_code):
        """编辑悬停位置定位"""
        return "//tr[contains(.,'" + course_code + "')]//i[contains(@class,'action-icon')]"

    def edit_button(self, course_code):
        """编辑按钮定位（根据课程代码）

        Args:
            course_code: 课程代码
        """
        return "//tr[contains(.,'" + course_code + "')]//button"

    def delete_button(self):
        """删除课程按钮定位"""
        return "//button[contains(.,'删除课程')]"

    def delete_confirm_button(self):
        """删除确认按钮定位"""
        return "//div[contains(.,'警告')]//button[contains(.,'确定')]"

    def delete_success_alert(self):
        """删除成功提示框"""
        return "//p[contains(.,'删除成功')]"

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
            return "//textarea[contains(@placeholder,'课程描述')]"
        else:
            return None

    def new_course_dept_dropdown(self):
        """所属学院下拉框"""
        return "//div[@aria-label='新建课程']//span[text()='请选择学院']/parent::div"

    def new_course_dept_dropdown_option(self, dept_name):
        """所属学院下拉框选项"""
        return "//div[@aria-hidden='false']//span[contains(.,'" + dept_name + "')]/parent::li"

    def new_course_first_class_switch(self):
        """是否一流课程开关"""
        return "//div[./label[text()='是否一流课程']]/div/div"

    def new_course_responsible_person_dropdown(self):
        """课程负责人下拉框"""
        return "//div[@aria-label='新建课程']//span[text()='请选择课程负责人']/parent::div"

    def new_course_responsible_person_dropdown_option(self, prof_name):
        """课程负责人下拉框选项"""
        return "//span[text()='" + prof_name + "']/parent::div"

    def new_course_confirm_button(self):
        """新建确定按钮"""
        return "//button[contains(.,'确定')]"

    def create_success_alert(self):
        """创建成功提示框"""
        return "//p[text()='新建成功']"
