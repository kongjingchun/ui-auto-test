# encoding: utf-8
# @File  : UserManagePage.py.py
# @Author: 孔敬淳
# @Date  : 2025/12/25/14:33
# @Desc  : 用户管理页面对象类，封装用户管理相关的页面操作方法
from time import sleep

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.dean_manage.UserManageBase import UserManageBase
from common.yaml_config import GetConf
from logs.log import log


class UserManagePage(UserManageBase, ObjectMap):
    """用户管理页面类
    
    继承UserManageBase和ObjectMap类，提供用户管理页面的元素操作方法
    """

    def move_add_user_button(self, driver):
        """鼠标悬停到创建按钮
        
        Args:
            driver: WebDriver实例
            
        Returns:
            悬停操作结果
        """
        log.info("鼠标悬停到手动创建按钮")
        xpath = self.add_user_button()
        return self.action_move_to_element(driver, By.XPATH, xpath)

    def click_add_user_role_select(self, driver, role_name):
        """点击选择创建的用户角色身份
        Args:
            driver: WebDriver实例
            role_name: 角色名称（如：创建教务管理员、创建教师、创建学生）
        Returns:
            点击操作结果
        """
        log.info("创建的角色身份为：" + role_name)
        xpath = self.add_user_role_select(role_name)
        return self.element_click(driver, By.XPATH, xpath)

    def input_user_value(self, driver, input_name, value):
        """输入用户信息"""
        log.info(f"输入用户信息：{input_name}为：{value}")
        xpath = self.creat_user_input_xpath(input_name)
        return self.element_input_value(driver, By.XPATH, xpath, value)

    def click_submit_user_button(self, driver):
        """点击提交信息按钮
        Returns:
            点击操作结果
        """
        log.info("点击提交信息按钮")
        xpath = self.submit_user_button()
        return self.element_double_click(driver, By.XPATH, xpath)

    def is_create_success_alert_display(self, driver):
        """判断创建成功的提示框是否出现
        Returns:
            bool: True表示创建成功，False表示失败
        """
        log.info("判断创建成功的提示框是否出现")
        return self.element_is_display(driver, By.XPATH, self.create_success_alert())

    def input_search_input(self, driver, input_name, value):
        """向搜索输入框输入内容
        Args:
            driver: WebDriver实例
            input_name: 要填写的搜索方式
            value: 填入的值
        Returns:
            输入操作结果
        """
        log.info(f"通过{input_name}搜索{value}")
        return self.element_input_value(driver, By.XPATH, self.search_input(input_name), value)

    def click_user_bind_button(self, driver, user_name):
        """点击用户绑定按钮
        Args:
            driver: WebDriver实例
            user_name: 用户名
        Returns:
            点击操作结果
        """
        log.info(f"点击用户绑定按钮：{user_name}")
        return self.element_click(driver, By.XPATH, self.user_bind_button(user_name))

    def input_user_bind_input(self, driver, user_id):
        """输入用户绑定ID
        Args:
            driver: WebDriver实例
            user_id: 用户ID
        Returns:
            输入操作结果
        """
        log.info(f"输入用户绑定ID：{user_id}")
        return self.element_input_value(driver, By.XPATH, self.user_bind_input(), user_id)

    def click_user_bind_confirm_button(self, driver):
        """点击确认绑定
        Args:
            driver: WebDriver实例
        Returns:
            点击操作结果
        """
        log.info("点击确认绑定")
        return self.element_click(driver, By.XPATH, self.user_bind_confirm_button())

    def is_user_bind_success_alert_display(self, driver):
        log.info("判断绑定成功的提示框是否出现")
        return self.element_is_display(driver, By.XPATH, self.bind_success_alert())

    def create_user(self, driver, role_name, user_info):
        """创建用户
        Args:
            driver: WebDriver实例
            role_name: 创建的角色名称（如：创建教务管理员、创建教师、创建学生）
            user_info: 用户信息字典，key为字段名称，value为字段值
                      例如：{"姓名": "张三", "工号": "001", "手机": "13800138000", "邮箱": "test@example.com"}
        Returns:
            bool: True表示创建成功，False表示失败
        """
        self.switch_into_iframe(driver, By.XPATH, self.user_manage_iframe())
        self.move_add_user_button(driver)
        self.click_add_user_role_select(driver, role_name)

        # 根据user_info字典动态输入用户信息
        for input_name, value in user_info.items():
            self.input_user_value(driver, input_name, str(value))
        self.click_submit_user_button(driver)
        results = self.is_create_success_alert_display(driver)
        self.switch_out_iframe(driver)
        log.info("创建用户结果：" + str(results))
        return results

    # 绑定用户
    def bind_user(self, driver, user, user_id):
        """绑定用户
        Args:
            driver: WebDriver实例
            user: 用户名的一个信息：姓名、工号或手机号等
            user_id: 用户ID
        Returns:
            bool: True表示绑定成功，False表示失败
        """
        self.switch_into_iframe(driver, By.XPATH, self.user_manage_iframe())
        self.input_search_input(driver, "工号", user)
        self.click_user_bind_button(driver, user)
        self.input_user_bind_input(driver, user_id)
        self.click_user_bind_confirm_button(driver)
        result = self.is_user_bind_success_alert_display(driver)
        self.switch_out_iframe(driver)
        log.info("绑定用户结果：" + str(result))
        return result
