# encoding: utf-8
# @File  : TrainingProgramManageBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 培养方案管理页面元素定位基类

class TrainingProgramManageBase:
    """培养方案管理页面元素定位基类

    提供培养方案管理相关页面元素的XPath定位表达式
    """

    def training_program_manage_iframe(self):
        """培养方案管理iframe定位"""
        return "//iframe[@id='app-iframe-2102']"

    def new_training_program_button(self):
        """新建培养方案按钮"""
        return "//button[contains(.,'新建培养方案')]"

    def import_training_program_button(self):
        """导入培养方案按钮"""
        return "//button[contains(.,'导入培养方案')]"

    def search_keyword_input(self):
        """搜索关键词输入框"""
        return "//input[@placeholder='培养方案名称']"

    def new_training_program_input(self, input_name):
        """新建培养方案输入框定位

        Args:
            input_name: 输入框名称，如 '方案名称'、'学分要求'、'版本年份'
        """
        if '方案名称' in input_name or '名称' in input_name:
            return "//div[@aria-label='新建培养方案']//input[contains(@placeholder,'请输入培养方案名称')]"
        elif '学分要求' in input_name or '学分' in input_name:
            return "//div[@aria-label='新建培养方案']//label[contains(.,'学分要求')]/following-sibling::div//input"
        elif '版本年份' in input_name or '年份' in input_name:
            return "//div[@aria-label='新建培养方案']//label[contains(.,'版本年份')]/following-sibling::div//input"
        else:
            return None

    def new_training_program_major_dropdown(self):
        """关联专业下拉框"""
        return "//div[@aria-label='新建培养方案']//span[text()='请选择专业']/parent::div"

    def new_training_program_major_dropdown_option(self, major_name):
        """关联专业下拉框选项"""
        return "//div[@aria-hidden='false']//span[contains(.,'" + major_name + "')]/parent::li"

    def new_training_program_type_dropdown(self):
        """培养类型下拉框"""
        return "//div[@aria-label='新建培养方案']//span[text()='请选择培养类型']/parent::div"

    def new_training_program_type_dropdown_option(self, type_name):
        """培养类型下拉框选项"""
        return "//div[@aria-hidden='false']//span[contains(.,'" + type_name + "')]/parent::li"

    def new_training_program_level_dropdown(self):
        """培养层次下拉框"""
        return "//div[@aria-label='新建培养方案']//span[text()='请选择培养层次']/parent::div"

    def new_training_program_level_dropdown_option(self, level_name):
        """培养层次下拉框选项"""
        return "//div[@aria-hidden='false']//span[text()='" + level_name + "']/parent::li"

    def new_training_program_duration_dropdown(self):
        """学制下拉框"""
        return "//div[@aria-label='新建培养方案']//span[text()='请选择学制']/parent::div"

    def new_training_program_duration_dropdown_option(self, duration):
        """学制下拉框选项"""
        return "//div[@aria-hidden='false']//span[contains(.,'" + duration + "')]/parent::li"

    def new_training_program_degree_dropdown(self):
        """授予学位下拉框"""
        return "//div[@aria-label='新建培养方案']//span[text()='请选择授予学位']/parent::div"

    def new_training_program_degree_dropdown_option(self, degree_name):
        """授予学位下拉框选项"""
        return "//div[@aria-hidden='false']//span[contains(.,'" + degree_name + "')]/parent::li"

    def new_training_program_credit_increase_button(self):
        """学分要求增加按钮（+按钮）"""
        return "//div[@aria-label='新建培养方案']//label[contains(.,'学分要求')]/following-sibling::div//button[contains(.,'+') or contains(@class,'el-input-number__increase')]"

    def new_training_program_credit_decrease_button(self):
        """学分要求减少按钮（-按钮）"""
        return "//div[@aria-label='新建培养方案']//label[contains(.,'学分要求')]/following-sibling::div//button[contains(.,'-') or contains(@class,'el-input-number__decrease')]"

    def new_training_program_year_increase_button(self):
        """版本年份增加按钮（+按钮）"""
        return "//div[@aria-label='新建培养方案']//label[contains(.,'版本年份')]/following-sibling::div//button[contains(.,'+') or contains(@class,'el-input-number__increase')]"

    def new_training_program_year_decrease_button(self):
        """版本年份减少按钮（-按钮）"""
        return "//div[@aria-label='新建培养方案']//label[contains(.,'版本年份')]/following-sibling::div//button[contains(.,'-') or contains(@class,'el-input-number__decrease')]"

    def new_training_program_cancel_button(self):
        """新建培养方案取消按钮"""
        return "//div[@aria-label='新建培养方案']//button[contains(.,'取消')]"

    def new_training_program_create_button(self):
        """新建培养方案创建按钮"""
        return "//div[@aria-label='新建培养方案']//button[contains(.,'创建')]"

    def create_success_alert(self):
        """创建成功提示框"""
        return "//p[text()='创建培养方案成功']"
