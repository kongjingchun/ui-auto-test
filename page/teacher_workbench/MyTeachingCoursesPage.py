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
        """切换到我教的课iframe

        Args:
            driver: WebDriver实例

        Returns:
            切换操作结果
        """
        xpath = self.my_teaching_courses_iframe()
        log.info(f"切换到我教的课iframe，xpath定位为：{xpath}")
        return self.switch_into_iframe(driver, By.XPATH, xpath)

    def input_course_search(self, driver, course_name):
        """输入课程搜索关键词

        Args:
            driver: WebDriver实例
            keyword: 搜索关键词（课程代码或课程名称）

        Returns:
            输入操作结果
        """
        xpath = self.course_search_input()
        log.info(f"输入课程搜索关键词：{course_name}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, course_name)

    def click_course_card_by_name(self, driver, course_name, need_hover=False):
        """根据课程名称点击课程卡片

        Args:
            driver: WebDriver实例
            course_name: 课程名称

        Returns:
            点击操作结果
        """
        xpath = self.course_card_by_name(course_name)
        log.info(f"根据课程名称'{course_name}'点击课程卡片，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15, need_hover=need_hover)

    def click_course(self, driver, course_name):
        """点击课程

        Args:
            driver: WebDriver实例
            course_name: 课程名称

        Returns:
            点击操作结果
        """
        # 切换到我教的课iframe
        self.switch_into_my_teaching_courses_iframe(driver)
        # 输入课程搜索关键词
        self.input_course_search(driver, course_name)
        # 根据课程名称点击课程卡片
        self.click_course_card_by_name(driver, course_name, need_hover=True)
        # 切出我教的课iframe
        self.switch_out_iframe(driver)
        return True
