# encoding: utf-8
# @File  : MajorManageBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/30/16:23
# @Desc  :

class MajorManageBase:
    """专业管理页面元素定位基类"""

    def major_manage_iframe(self):
        """专业管理iframe定位"""
        return "//iframe[@id='app-iframe-2101']"

    def new_major_button(self):
        """新建专业按钮"""
        return "//button[contains(.,'新建专业')]"

    def new_dep_input(self, input_name):
        """
        新建专业输入框定位
        :param input_name: '代码' 或 '名称'
        """
        if '名称' in input_name:
            return "//input[contains(@placeholder,'请输入专业名称')]"
        elif '代码' in input_name and '学校' in input_name:
            return "//input[contains(@placeholder,'请输入专业代码（学校）')]"
        elif '代码' in input_name and '国家' in input_name:
            return "//input[contains(@placeholder,'请输入专业代码（国家）')]"

    def new_major_belong_dep_dropdown(self):
        """新建专业所属学院下拉点击框"""
        return "//span[text()='请选择所属院系']/parent::div"


