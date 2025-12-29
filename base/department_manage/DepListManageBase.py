# encoding: utf-8
# @File  : DepListManageBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/29/16:24
# @Desc  : 院系列表管理

class DepListManageBase:
    """院系列表管理页面元素定位基类"""

    def dep_manage_iframe(self):
        """获取院系管理页面的iframe定位"""
        return "//iframe[@id='app-iframe-3004']"

    # 新建院系xpath
    def new_dep_button(self):
        return "//button[contains(.,'新建院系')]"
