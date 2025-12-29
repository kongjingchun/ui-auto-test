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
        return "//iframe[@id='app-iframe-2006']"

    def add_user_button(self):
        """获取手动新增按钮的XPath定位表达式"""
        return "//div[@class='el-dropdown toolbar-button']"

    def add_user_role_select(self, role_name):
        """选择创建角色身份的XPath定位表达式"""
        return "//li[contains(.,'" + role_name + "')]"
        # return "//li[contains(., '" + role_name + "') and div[@class='role-item']]"

    def creat_user_input_xpath(self, input_name):
        """信息填写的Xpath定位表达式"""
        return "//div[contains(@aria-label,'创建')]//input[contains(@placeholder,'" + input_name + "')]"

    def submit_user_button(self):
        """创建用户按钮的Xpath定位表达式"""
        return "//div[@class = 'dialog-footer']/button[contains(.,'创建用户')]"

    def create_success_alert(self):
        """创建成功提示框的Xpath定位表达式"""
        return "//p[contains(text(),'创建成功')]"

    def search_input(self, input_name):
        """搜索框的Xpath定位表达式"""

        return "//input[contains(@placeholder,'" + input_name + "')]"

    def user_bind_button(self, user_name):
        """用户绑定按钮的Xpath定位表达式"""
        return "//span[contains(text(),'" + user_name + "')]/ancestor::td/following-sibling ::td//div[@class='action-buttons']//button[contains(.,'绑定')]"

    def user_bind_input(self):
        """绑定用户平台ID输入框的Xpath定位表达式"""
        return "//input[@placeholder='请输入平台用户ID']"

    def user_bind_confirm_button(self):
        """确认绑定按钮的Xpath定位表达式"""
        return "//span[contains(.,'确认绑定')]/parent::button"

    #     绑定成功提示
    def bind_success_alert(self):
        """绑定成功提示框的Xpath定位表达式"""
        return "//p[contains(text(),'绑定用户成功')]"
