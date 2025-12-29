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
