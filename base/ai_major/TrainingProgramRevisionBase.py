# encoding: utf-8
# @File  : TrainingProgramRevisionBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 培养方案修订页面元素定位基类

class TrainingProgramRevisionBase:
    """培养方案修订页面元素定位基类

    提供培养方案修订相关页面元素的XPath定位表达式
    包含6个子页面：专业信息、培养目标、毕业要求、课程设置、实践教学、课程支撑
    """
    # ==================== 通用元素 ====================

    def revision_tab(self, tab_name):
        """修订页面标签页定位

        Args:
            tab_name: 标签页名称，如 '专业信息'、'培养目标'、'毕业要求'、'课程设置'、'实践教学'、'课程支撑'
        """
        return "//span[text()='" + tab_name + "']/parent::div"

    def save_button(self):
        """保存按钮"""
        return "//button[contains(.,'保存')]"

    def cancel_button(self):
        return "//button[contains(.,'取消')]"

    def save_success_alert(self):
        """保存成功断言"""
        return "//p[text()='保存成功']"

    # ==================== 专业信息页面 ====================

    def major_description_input(self):
        """专业描述输入框"""
        return "//textarea[contains(@placeholder,'专业概述')]"

    # ==================== 培养目标页面 ====================
    def training_objective_overview_textarea(self):
        """培养目标概述文本域"""
        return "//textarea[contains(@placeholder,'培养目标概述') or contains(@placeholder,'请输入培养目标概述')]"

    def add_training_objective_button(self):
        """添加目标按钮"""
        return "//button[contains(.,'添加目标')]"

    def training_objective_description_textarea(self):
        """培养目标描述文本域"""
        return "//textarea[contains(@placeholder,'培养目标描述') or contains(@placeholder,'请输入培养目标描述')]"

    def training_objective_save_button(self):
        """培养目标保存按钮"""
        return "//div[./button[contains(.,'取消')]]/button[contains(.,'保存')]"

    # ==================== 毕业要求页面 ====================
    def graduation_requirement_description_textarea(self):
        """毕业要求描述文本域"""
        return "//textarea[contains(@placeholder,'毕业要求概述')]"

    def add_indicator_point_button(self):
        """添加指标点按钮"""
        return "//button[contains(.,'添加指标点')]"

    def indicator_point_name_input(self, indicator_index=1):
        """指标点名称输入框

        Args:
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）
        """
        return "//div[@class = 'requirements-list']/div[" + str(indicator_index) + "]//input[@placeholder='指标点名称']"

    def indicator_point_description_textarea(self, indicator_index=1):
        """指标点描述文本域

        Args:
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）
        """
        return "//div[@class = 'requirements-list']/div[" + str(indicator_index) + "]//textarea[contains(@placeholder,'指标点')]"
    # 展开button

    def expand_button(self, indicator_index=1):
        """展开按钮

        Args:
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）
        """
        return "//div[@class = 'requirements-list']/div[" + str(indicator_index) + "]//button[contains(.,'展开')]"

    def add_decomposed_indicator_point_button(self, indicator_index=1):
        """添加分解指标点按钮

        Args:
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）
        """
        return "//div[@class = 'requirements-list']/div[" + str(indicator_index) + "]//button[contains(.,'添加分解指标点')]"

    def decomposed_indicator_point_name_input(self, indicator_index=1, decomposed_index=1):
        """分解指标点名称输入框

        Args:
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）
            decomposed_index: 分解指标点序号，从1开始，默认为1（第1个分解指标点）
        """
        return "//div[@class = 'requirements-list']/div[" + str(indicator_index) + "]//div[@class='sub-requirements-list']/div[" + str(decomposed_index) + "]//input[@placeholder='分解指标点名称']"

    def decomposed_indicator_point_description_textarea(self, indicator_index=1, decomposed_index=1):
        """分解指标点描述文本域

        Args:
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）
            decomposed_index: 分解指标点序号，从1开始，默认为1（第1个分解指标点）
        """
        return "//div[@class = 'requirements-list']/div[" + str(indicator_index) + "]//div[@class='sub-requirements-list']/div[" + str(decomposed_index) + "]//textarea[contains(@placeholder,'分解指标点')]"

    # ==================== 目标支撑页面 ====================
    # 目标支撑选择按钮
    def target_support_select_button(self, index=1):
        """目标支撑选择按钮

        Args:
            index: 选择按钮序号，从1开始，默认为1（第1个选择按钮）
        """
        return "(//span[text()='选择'])[" + str(index) + "]"
    # 支撑等级，有高支撑、中支撑、低支撑无支撑4个选项

    def target_support_level_option(self, level="高支撑"):
        """目标支撑等级选项

        Args:
            level: 支撑等级，有高支撑、中支撑、低支撑无支撑4个选项
        """
        return "//div[@aria-hidden='false']//span[contains(.,'" + level + "')]"
    # ==================== 课程设置页面 ====================

    # ==================== 实践教学页面 ====================

    # ==================== 课程支撑页面 ====================
