# encoding: utf-8
# @File  : LoginBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/01/18:01
# @Desc  :登录页面元素定位


class LoginBase:
    @staticmethod
    def login_input(input_placeholder):
        """
        登录用户名、密码输入框
        :param input_placeholder:
        :return:
        """
        return "//input[@placeholder='" + input_placeholder + "']"

    @staticmethod
    def login_button(button_name):
        """
        登录按钮
        :return:
        """
        return "//span[text()='" + button_name + "']/parent::button"

    @staticmethod
    def login_successful():
        """
        登录成功提示
        :return:
        """
        return "//p[text()='登录成功']"

    @staticmethod
    def need_captcha():
        """
        验证码勾选框
        :return:
        """
        return "//span[@class='el-checkbox__inner']"

    def captcha(self):
        """
        验证码
        :return:
        """
        return "//img[@class='el-image__inner']"



if __name__ == '__main__':
    print(LoginBase().login_input("用户名"))
    print(LoginBase().login_button("登录"))
