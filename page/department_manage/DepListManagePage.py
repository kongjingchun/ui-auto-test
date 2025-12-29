# encoding: utf-8
# @File  : DepListManagePage.py.py
# @Author: 孔敬淳
# @Date  : 2025/12/29/16:27
# @Desc  : 院系列表管理
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.department_manage.DepListManageBase import DepListManageBase
from logs.log import log


class DepListManagePage(DepListManageBase, ObjectMap):
    """院系列表管理页面类

    继承DepListManageBase和ObjectMap类，提供院系列表管理页面元素操作方法
    """

    def switch_2_dep_manage_iframe(self, driver):
        """切换到院系列表管理页面的iframe

        Returns:
            切换操作结果
        """
        log.info("切换到院系列表管理页面的iframe")
        return self.switch_into_iframe(driver, By.XPATH, self.dep_manage_iframe())
