# encoding: utf-8
# @File  : CmsUserManagePage.py
# @Author: 孔敬淳
# @Date  : 2025/12/26/14:11
# @Desc  : CMS用户管理页面对象类，封装CMS用户管理相关的页面操作方法
import requests
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.cms.CmsUserManageBase import CmsUserManageBase
from common.yaml_config import GetConf
from logs.log import log


class CmsUserManage(CmsUserManageBase, ObjectMap):
    """CMS用户管理页面类

    继承CmsUserManageBase和ObjectMap类，提供CMS用户管理页面的元素操作方法
    """

    # 接口注册CMS用户
    def register_cms_user(self, user_info):
        """通过API注册CMS用户

        Args:
            user_info: 用户信息字典，包含username和password键
                      例如：{"username": "test_user", "password": "test_password"}

        Returns:
            bool: True表示注册成功，False表示注册失败
        """
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
        """切换到CMS用户管理iframe

        Args:
            driver: WebDriver实例

        Returns:
            切换iframe操作结果
        """
        iframe_xpath = self.cms_user_manage_iframe()
        log.info(f"进入用户管理iframe，xpath定位为：{iframe_xpath}")
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def input_search_value(self, driver, value):
        """在搜索输入框中输入内容

        Args:
            driver: WebDriver实例
            value: 要搜索的值

        Returns:
            输入操作结果
        """
        search_input_xpath = self.search_input()
        log.info(f"在搜索框中输入内容查询：{value}，xpath定位为：{search_input_xpath}")
        return self.element_input_value(driver, By.XPATH, search_input_xpath, value)

    def input_search_keyword(self, driver, keyword):
        """输入搜索关键词

        Args:
            driver: WebDriver实例
            keyword: 搜索关键词（用户名、昵称或手机号）

        Returns:
            输入操作结果
        """
        xpath = self.search_keyword_input()
        log.info(f"输入搜索关键词：{keyword}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, keyword)

    def switch_out_cms_iframe(self, driver):
        """退出CMS用户管理iframe

        Args:
            driver: WebDriver实例

        Returns:
            退出iframe操作结果
        """
        log.info("退出iframe")
        return self.switch_out_iframe(driver)

    def search_cms_user(self, driver, username):
        """搜索CMS用户并获取用户ID

        Args:
            driver: WebDriver实例
            username: 用户名

        Returns:
            str: 用户ID，如果未找到则返回None
        """
        log.info(f"搜索用户:{username}")
        self.switch_2_cms_user_manage_iframe(driver)
        self.input_search_value(driver, username)
        user_id_xpath = self.get_user_id_xpath(username)
        log.info(f"获取用户ID，xpath定位为：{user_id_xpath}")
        user_id = self.get_element_text(driver, By.XPATH, user_id_xpath)
        self.switch_out_cms_iframe(driver)
        return user_id

    def hover_edit_button(self, driver, username):
        """鼠标悬停编辑按钮

        Args:
            driver: WebDriver实例
            username: 用户名

        Returns:
            悬停操作结果
        """
        xpath = self.edit_button_hover_location(username)
        log.info(f"鼠标悬停编辑按钮，xpath定位为：{xpath}")
        return self.element_hover(driver, By.XPATH, xpath)

    def click_edit_button_by_username(self, driver, username):
        """根据用户名点击编辑按钮

        Args:
            driver: WebDriver实例
            username: 用户名

        Returns:
            点击操作结果
        """
        xpath = self.edit_button(username)
        log.info(f"根据用户名'{username}'点击编辑按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

    def click_delete_button(self, driver):
        """点击删除用户按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.delete_button()
        log.info(f"点击删除用户按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

    def click_delete_confirm_button(self, driver):
        """点击删除确认按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.delete_confirm_button()
        log.info(f"点击删除确认按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

    def is_delete_success_alert_display(self, driver):
        """查看删除成功提示框是否出现

        Args:
            driver: WebDriver实例

        Returns:
            bool: True表示删除成功提示框出现，False表示未出现
        """
        xpath = self.delete_success_alert()
        log.info(f"查看删除成功提示框是否出现，xpath定位为：{xpath}")
        return self.element_is_display(driver, By.XPATH, xpath)

    def delete_cms_user_by_username(self, driver, username):
        """根据用户名删除CMS用户

        Args:
            driver: WebDriver实例
            username: 用户名

        Returns:
            bool: True表示删除成功，False表示删除失败
        """
        # 切换到iframe
        self.switch_2_cms_user_manage_iframe(driver)
        # 输入搜索关键词
        self.input_search_keyword(driver, username)
        # 鼠标悬停编辑按钮
        self.hover_edit_button(driver, username)
        # 点击编辑按钮
        self.click_edit_button_by_username(driver, username)
        # 点击删除按钮
        self.click_delete_button(driver)
        # 点击删除确认按钮
        self.click_delete_confirm_button(driver)
        # 断言删除成功提示框是否出现
        result = self.is_delete_success_alert_display(driver)
        # 切出iframe
        self.switch_out_cms_iframe(driver)
        log.info(f"删除CMS用户结果：{result}")
        return result


if __name__ == '__main__':
    res = CmsUserManage().register_cms_user("dean_cms")
