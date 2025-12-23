# encoding: utf-8
# @File  : AccountBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/17/17:10
# @Desc  :

class AccountBase:
    def basic_info_avatar_input(self):
        return "//div[@class='avatar-uploader']//input"

    def basic_info_save_button(self):
        return "//span[text()='保存']/parent::button"
