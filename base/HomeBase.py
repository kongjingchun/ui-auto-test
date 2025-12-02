# encoding: utf-8
# @File  : HomeBase.py
# @Author: kongjingchun
# @Date  : 2025/12/02/16:05
# @Desc  :首页元素定位

class HomeBase:
    @staticmethod
    def wallet_switch():
        """
        钱包开关
        :return:
        """
        return "//span[contains(@class,'switch')]"

    @staticmethod
    def logo():
        """
        logo定位
        :return:
        """
        return "//div[contains(text(),'二手交易')]"

    @staticmethod
    def welcome():
        """
        首页，欢迎您回来
        :return:
        """
        return "//span[starts-with(text(),'回来')]"