# encoding: utf-8
# @File  : MyTeachingCoursesPage.py
# @Author:
# @Date  :
# @Desc  : 我教的课页面对象类，封装我教的课相关的页面操作方法

from time import sleep

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.teacher_workbench.MyTeachingCoursesBase import MyTeachingCoursesBase
from logs.log import log


class MyTeachingCoursesPage(MyTeachingCoursesBase, ObjectMap):
    """我教的课页面类

    继承MyTeachingCoursesBase和ObjectMap类，提供我教的课页面的元素操作方法
    """

    def switch_into_my_teaching_courses_iframe(self, driver):
        """切换到我教的课iframe"""
        xpath = self.my_teaching_courses_iframe()
        log.info(f"切换到我教的课iframe，xpath定位为：{xpath}")
        return self.switch_into_iframe(driver, By.XPATH, xpath)
