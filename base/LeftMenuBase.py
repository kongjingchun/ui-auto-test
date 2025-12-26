# encoding: utf-8
# @File  : LeftMenuBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/25/12:02
# @Desc  : 左侧菜单元素定位基类

class LeftMenuBase:
    """左侧菜单元素定位基类"""

    def two_level_menu(self, menu_name):
        """二级菜单定位"""
        return "//div[text()='" + menu_name + "']/parent::div"
