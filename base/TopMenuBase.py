# encoding: utf-8
# @File  : TopMenuBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/21:48
# @Desc  : 顶部菜单元素定位基类

class TopMenuBase:
    """顶部菜单元素定位基类
    
    提供顶部菜单相关页面元素的XPath定位表达式
    """

    def school_switch(self):
        """学校切换按钮定位"""
        return "//div[@class='el-dropdown org-dropdown']"

    def school_switch_list(self, school_name):
        """学校切换列表定位"""
        return "//span[text()='" + school_name + "']/ancestor::li"

    def role_switch(self):
        """角色切换按钮定位"""
        return "//div[@class='role-tag']"

    def role_switch_list(self, role_name):
        """角色切换列表定位"""
        return "//span[text()='" + role_name + "']//ancestor::li"
