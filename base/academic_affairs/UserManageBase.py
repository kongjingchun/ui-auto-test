# encoding: utf-8
# @File  : UserManageBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/25/11:59
# @Desc  :

class UserManageBase:
    """用户管理元素定位基类

    提供用户管理相关页面元素的XPath定位表达式
    """


    def user_manage_iframe(self):
        """获取用户管理页面的iframe的XPath定位表达式"""
        return "//iframe"

    def add_user_button(self):
        """获取手动新增按钮的XPath定位表达式"""
        return "//div[@class='el-dropdown toolbar-button']"

    def add_user_role_select(self, role_name):
        """选择创建角色身份的XPath定位表达式"""
        return "//li[contains(.,'教务管理员')]"
        # return "//li[contains(., '" + role_name + "') and div[@class='role-item']]"

    def input_user_value(self, input_name):
        """信息填写的Xpath定位表达式"""
        return "//div[contains(@aria-label,'创建')]//input[contains(@placeholder,'" + input_name + "')]"

    def submit_user_button(self):
        """创建用户按钮的Xpath定位表达式"""
        return "//div[@class = 'dialog-footer']/button[contains(.,'创建用户')]"
