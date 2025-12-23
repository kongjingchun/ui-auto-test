# encoding: utf-8
# @File  : IframeBaiduMapBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/17/17:49
# @Desc  :
class IframeBaiduMapBase:
    def search_input(self):
        """
        搜索输入框
        :return:
        """
        return "//input[@id='sole-input']"

    def search_button(self):
        """
        搜索按钮
        :return:
        """
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        """
        百度地图 iframe
        :return:
        """
        return "//iframe[@src='https://map.baidu.com/']"