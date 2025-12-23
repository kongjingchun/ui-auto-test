# encoding: utf-8
# @File  : ExternalLinkPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/17/16:14
# @Desc  :
from base.ObjectMap import ObjectMap


class ExternalLinkPage(ObjectMap):
    def goto_imooc(self, driver):
        self.switch_windows_2_latest_handle(driver)
        return driver.title
