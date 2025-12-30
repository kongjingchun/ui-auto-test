# encoding: utf-8
# @File  : MajorManageBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/30/16:23
# @Desc  :

class MajorManageBase:
    """专业管理页面元素定位基类"""

    def major_manage_iframe(self):
        """专业管理iframe"""
        return "//iframe[@id='app-iframe-2101']"

    def new_major_button(self):
        """新建专业按钮"""
        return "//button[contains(.,'新建专业')]"

    def new_major_input(self, input_name):
        """新建专业输入框"""
        if '名称' in input_name:
            return "//input[contains(@placeholder,'请输入专业名称')]"
        elif '代码' in input_name and '学校' in input_name:
            return "//input[contains(@placeholder,'请输入专业代码（学校）')]"
        elif '代码' in input_name and '国家' in input_name:
            return "//input[contains(@placeholder,'请输入专业代码（国家）')]"

    def new_major_belong_dep_dropdown(self):
        """所属院系下拉框"""
        return "//span[text()='请选择所属院系']/parent::div"

    def new_major_belong_dep_dropdown_option(self, dept_name):
        """所属院系下拉框选项"""
        return "//div[@aria-hidden='false']//span[text()='" + dept_name + "']/parent::li"

    def new_major_belong_prof_dropdown(self):
        """专业负责人下拉框"""
        return "//span[text()='请选择专业负责人']/parent::div"

    def new_major_belong_prof_dropdown_option(self, prof_name):
        """专业负责人下拉框选项"""
        return "//span[text()='" + prof_name + "']/parent::li"

    def new_major_build_level_radio(self, level="国家一流本科专业"):
        """建设层次单选框"""
        if "国" in level:
            return "//span[text()='国家一流本科专业']/preceding-sibling::span"
        elif "普" in level:
            return "//span[text()='普通专业']/preceding-sibling::span"
        elif "省" in level:
            return "//span[text()='省级一流本科专业']/preceding-sibling::span"
        elif "校" in level:
            return "//span[text()='校级重点专业']/preceding-sibling::span"

    def new_major_feature_checkbox(self, feature="国家级特色专业"):
        """特色专业复选框"""
        return "//span[text()='" + feature + "']/preceding-sibling::span"

    def new_major_confirm_button(self):
        """确认按钮"""
        return "//span[text()='确定']/parent::button"

    def create_success_alert(self):
        """创建成功提示框"""
        return "//p[text()='新建成功']"
