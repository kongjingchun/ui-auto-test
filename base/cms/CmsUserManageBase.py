# encoding: utf-8
# @File  : CmsUserManageBase.py.py
# @Author: 孔敬淳
# @Date  : 2025/12/26/14:11
# @Desc  :

class CmsUserManageBase:
    def cms_user_manage_iframe(self):
        """获取全部用户管理的xpath定位表达式"""
        return "//iframe"

    def search_input(self):
        """获取搜索输入框的xpath定位表达式"""
        return "//input[contains(@placeholder,'用户名')]"

