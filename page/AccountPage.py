# encoding: utf-8
# @File  : AccountPage.py
# @Author: kongjingchun
# @Date  : 2025/12/17/17:18
# @Desc  :
from selenium.webdriver.common.by import By

from base.AccountBase import AccountBase
from base.ObjectMap import ObjectMap
from common.tools import get_img_path


class AccountPage(AccountBase, ObjectMap):
    def upload_avatar(self, driver, img_name):
        file_path = get_img_path(img_name)
        import_xpath = self.basic_info_avatar_input()
        return self.upload(driver, By.XPATH, import_xpath, file_path)

    def click_save(self, driver):
        button_xpath = self.basic_info_save_button()
        return self.element_click(driver, By.XPATH, button_xpath)
