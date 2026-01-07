# encoding: utf-8
# @File  : CourseWorkbenchPage.py
# @Author:
# @Date  :
# @Desc  : 课程工作台页面对象类，封装课程工作台相关的页面操作方法

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.teacher_workbench.CourseWorkbenchBase import CourseWorkbenchBase
from logs.log import log


class CourseWorkbenchPage(CourseWorkbenchBase, ObjectMap):
    """课程工作台页面类

    继承CourseWorkbenchBase和ObjectMap类，提供课程工作台页面的元素操作方法
    """

    def switch_into_course_workbench_iframe(self, driver):
        """切换到课程工作台iframe

        Args:
            driver: WebDriver实例

        Returns:
            切换操作结果
        """
        xpath = self.course_workbench_iframe()
        log.info(f"切换到课程工作台iframe，xpath定位为：{xpath}")
        return self.switch_into_iframe(driver, By.XPATH, xpath)

