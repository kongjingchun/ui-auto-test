# encoding: utf-8
# @File  : LeftMenuBase.py
# @Author: kongjingchun
# @Date  : 2025/12/15/15:36
# @Desc  :

class LeftMenuBase:
    def level_one_menu(self, menu_name):
        """
        一级菜单栏
        :param menu_name:菜单栏名称
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']"



    def level_two_menu(self, menu_name):
        """
        二级菜单栏
        :param menu_name:菜单栏名称
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/parent::li"


if __name__ == '__main__':
    print(LeftMenuBase().level_one_menu("已卖出的宝贝"))
