# encoding: utf-8
# @File  : MajorPortalManageBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 专业门户管理页面元素定位基类

class MajorPortalManageBase:
    """专业门户管理页面元素定位基类

    提供专业门户管理相关页面元素的XPath定位表达式
    """

    def major_portal_manage_iframe(self):
        """专业门户管理iframe定位"""
        return "//iframe[@id='app-iframe-2104']"

    def search_keyword_input(self):
        """搜索关键词输入框"""
        return "//input[@placeholder='专业名称 ｜ 专业代码']"

    def search_button(self):
        """搜索按钮"""
        return "//button[contains(.,'搜索')]"

    def open_portal_button_by_major_name(self, major_name):
        """根据专业名称定位打开门户按钮

        Args:
            major_name: 专业名称
        """
        return "//tr[.//td[contains(.,'" + major_name + "')]]//button[contains(.,'打开门户')]"

    def edit_button_by_major_name(self, major_name):
        """根据专业名称定位编辑按钮

        Args:
            major_name: 专业名称
        """
        return "//tr[.//td[contains(.,'" + major_name + "')]]//button[contains(.,'编辑')]"

    def tab_by_index(self, index=1):
        """根据索引定位标签页

        Args:
            index: 标签页索引，从1开始，默认为1（第1个标签页）
        """
        return "(//span[contains(.,'专业门户管理')])[" + str(index) + "]"


# ======================================= 编辑页面元素定位 =======================================


    def major_portal_edit_iframe(self):
        """专业门户管理编辑页iframe定位"""
        return "//iframe[@id='app-iframe-3005']"

    def header_navigation_bar(self):
        """头部导航栏元素定位"""
        return "//div[@class='page-header']"

    def edit_page_button(self):
        """编辑页面按钮定位"""
        return "//button[contains(.,'编辑页面')]"

    def navigation_name_input(self, index=1):
        """导航名称设置输入框元素定位"""
        return "(//label[text()='名称'])[" + str(index) + "]/following-sibling::div//input"

    def publish_button(self):
        """发布按钮定位"""
        return "//button[contains(.,'发布')]"

    def publish_confirm_button(self):
        """发布确认按钮定位"""
        return "//div[@aria-label='发布确认']//button[contains(.,'确定')]"

    def open_portal_link_in_edit_page(self):
        """编辑页打开专业门户链接定位"""
        return "//a[contains(.,' 打开专业门户 ')]"
