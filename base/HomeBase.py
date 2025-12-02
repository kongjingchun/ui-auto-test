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

    @staticmethod
    def show_data():
        """
        日期显示
        :return:
        """
        return "//div[text()='我的日历']/following-sibling::div"

    @staticmethod
    def home_user_avata():
        """
        用户头像
        :return:
        """
        return "//span[contains(text(),'欢迎')]/parent::div/preceding-sibling::div//img"

    @staticmethod
    def home_user_avata2():
        """
        用户头像
        :return:
        """
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'avatar')]//img"
