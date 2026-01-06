# encoding: utf-8
# @File  : LoginBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/21:12
# @Desc  : 登录页面元素定位基类

class LoginBase:
    """登录页面元素定位基类

    提供登录相关页面元素的XPath定位表达式
    """

    def login_input(self, input_name):
        """获取登录输入框的XPath定位表达式

        Args:
            input_name: 输入框名称(账户、密码)

        Returns:
            str: XPath定位表达式
        """
        return f"//input[@placeholder='请输入您的{input_name}']"

    def login_button(self):
        """获取登录按钮的XPath定位表达式

        Returns:
            str: XPath定位表达式
        """
        return "//span[text()='登录']/parent::button"
# ==============================初始化密码==============================

    def new_password_input(self):
        """获取新密码输入框的XPath定位表达式

        Returns:
            str: XPath定位表达式
        """
        return "//input[@placeholder='请输入新密码（至少6位）']"

    def confirm_password_input(self):
        """获取确认密码输入框的XPath定位表达式

        Returns:
            str: XPath定位表达式
        """
        return "//input[@placeholder='请再次输入新密码']"

    def new_password_confirm_button(self):
        """获取确认修改按钮的XPath定位表达式

        Returns:
            str: XPath定位表达式
        """
        return "//span[text()=' 确认修改 ']/parent::button"
