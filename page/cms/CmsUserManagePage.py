# encoding: utf-8
# @File  : CmsUserManagePage.py
# @Author: 孔敬淳
# @Date  : 2025/12/26/14:11
# @Desc  :
import requests
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.cms.CmsUserManageBase import CmsUserManageBase
from common.yaml_config import GetConf
from logs.log import log


class CmsUserManage(CmsUserManageBase, ObjectMap):
    """CMS用户管理类

    继承UserManageBase类，提供CMS用户管理相关的页面操作方法
    """

    # 接口注册CMS用户
    def register_cms_user(self, user_info):
        """注册CMS用户"""
        username = user_info["username"]
        password = user_info["password"]
        log.info("api注册cms用户:用户名：" + username + "密码：" + password)
        data = {
            "username": str(username),
            "password": str(password)
        }
        url = GetConf().get_url()
        res = requests.post(url + "api/auth/register", json=data)
        response_data = res.json()

        # 判断返回结果中是否包含"注册成功"
        if "注册成功" in str(response_data):
            log.info(f"用户 {username} 注册成功")
            return True
        else:
            error_msg = f"用户 {username} 注册失败，返回结果：{response_data}"
            log.error(error_msg)
            return False

    def switch_2_cms_user_manage_iframe(self, driver):
        """进入用户管理iframe"""
        iframe_xpath = self.cms_user_manage_iframe()
        log.info(f"进入用户管理iframe，xpath定位为：{iframe_xpath}")
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def input_search_value(self, driver, value):
        """在搜索框中输入内容并查询"""
        search_input_xpath = self.search_input()
        log.info(f"在搜索框中输入内容查询：{value}，xpath定位为：{search_input_xpath}")
        return self.element_input_value(driver, By.XPATH, search_input_xpath, value)

    def switch_out_cms_iframe(self, driver):
        """退出cms_iframe"""
        log.info("退出iframe")
        return self.switch_out_iframe(driver)

    def search_cms_user(self, driver, username):
        """搜索用户"""
        log.info(f"搜索用户:{username}")
        self.switch_2_cms_user_manage_iframe(driver)
        self.input_search_value(driver, username)
        user_id_xpath = self.get_user_id_xpath(username)
        log.info(f"获取用户ID，xpath定位为：{user_id_xpath}")
        user_id = self.get_element_text(driver, By.XPATH, user_id_xpath)
        self.switch_out_cms_iframe(driver)
        return user_id


if __name__ == '__main__':
    res = CmsUserManage().register_cms_user("dean_cms")
