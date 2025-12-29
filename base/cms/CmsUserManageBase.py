# encoding: utf-8
# @File  : CmsUserManageBase.py.py
# @Author: 孔敬淳
# @Date  : 2025/12/26/14:11
# @Desc  :

class CmsUserManageBase:
    def cms_user_manage_iframe(self):
        """进入全部用户管理iframe的xpath定位表达式"""
        return "//iframe"

    def search_input(self):
        """获取搜索输入框的xpath定位表达式"""
        return "//input[contains(@placeholder,'用户名')]"

    # 获取用户ID的xpath
    def get_user_id_xpath(self, username):
        """获取用户ID的xpath"""
        return "//span[text()='" + username + "']/ancestor::td/preceding-sibling::td//span"
