# encoding: utf-8
# @File  : CmsUserManageBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/26/14:11
# @Desc  : CMS用户管理页面元素定位基类

class CmsUserManageBase:
    """CMS用户管理页面元素定位基类

    提供CMS用户管理相关页面元素的XPath定位表达式
    """

    def cms_user_manage_iframe(self):
        """CMS用户管理iframe的XPath定位表达式"""
        return "//iframe"

    def search_input(self):
        """搜索输入框的XPath定位表达式"""
        return "//input[contains(@placeholder,'用户名')]"

    def search_keyword_input(self):
        """搜索关键词输入框的XPath定位表达式"""
        return "//input[contains(@placeholder,'用户名 ｜ 昵称 ｜ 手机号')]"

    def get_user_id_xpath(self, username):
        """获取用户ID的xpath定位表达式

        Args:
            username: 用户名

        Returns:
            用户ID的XPath定位表达式
        """
        return "//span[text()='" + username + "']/ancestor::td/preceding-sibling::td//span"

    def edit_button_hover_location(self, username):
        """编辑按钮悬停位置的XPath定位表达式（根据用户名）

        Args:
            username: 用户名

        Returns:
            编辑按钮悬停位置的XPath定位表达式
        """
        return "//tr[contains(.,'" + username + "')]//i[contains(@class,'action-icon')]"

    def edit_button(self, username):
        """编辑按钮的XPath定位表达式（根据用户名）

        Args:
            username: 用户名

        Returns:
            编辑按钮的XPath定位表达式
        """
        return "//tr[contains(.,'" + username + "')]//button"

    def delete_button(self):
        """删除用户按钮的XPath定位表达式"""
        return "//button[contains(.,'删除用户')]"

    def delete_confirm_button(self):
        """删除确认按钮的XPath定位表达式"""
        return "//div[contains(.,'警告')]//button[contains(.,'确定')]"

    def delete_success_alert(self):
        """删除成功提示框的XPath定位表达式"""
        return "//p[contains(.,'删除成功')]"
