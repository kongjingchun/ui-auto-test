# encoding: utf-8
# @File  : MajorAIModelBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 专业AI模型页面元素定位基类

class MajorAIModelBase:
    """专业AI模型页面元素定位基类

    提供专业AI模型相关页面元素的XPath定位表达式
    """
    pass

    def major_ai_model_iframe(self):
        """专业AI模型iframe"""
        return "//iframe[@id='app-iframe-2110']"

    # 菜单定位根据名字定位
    def menu_by_name(self, menu_name):
        """菜单定位根据名字定位

        Args:
            menu_name: 菜单名称
        """
        return "//span[text()='" + menu_name + "']/parent::li"
