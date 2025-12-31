# encoding: utf-8
# @File  : RoleManageBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 角色管理页面元素定位基类

class RoleManageBase:
    """角色管理页面元素定位基类

    提供角色管理相关页面元素的XPath定位表达式
    """

    def role_manage_iframe(self):
        """角色管理iframe定位"""
        return "//iframe[@id='app-iframe-2008']"

    def assign_role_button(self, role_name):
        """分配角色按钮"""
        return "//tbody//tr[contains(.,'" + role_name + "')]//span[contains(.,'分配')]/parent::button"

    def user_search_input(self):
        """用户搜索输入框"""
        return "//input[contains(@placeholder,'用户ID')]"

    def user_checkbox(self, user_name):
        """勾选用户复选框"""
        return "//tr[contains(.,'" + user_name + "')]//span[@class='el-checkbox__inner']"

    def assign_role_confirm_button(self):
        """分配角色确认按钮"""
        return "//button[.//span[contains(.,'确定分配')]]"

    def assign_role_success_alert(self):
        """分配角色成功提示框"""
        return "//p[contains(text(),'成功')]"
