# encoding: utf-8
# @File  : CourseWorkbenchBase.py
# @Author:
# @Date  :
# @Desc  : 课程工作台页面元素定位基类

class CourseWorkbenchBase:
    """课程工作台页面元素定位基类

    提供课程工作台相关页面元素的XPath定位表达式
    """
    pass

    def course_workbench_iframe(self):
        """课程工作台iframe"""
        return "//iframe[@id='app-iframe-4002']"

    def menu_by_name(self, menu_name):
        """菜单定位根据名字定位

        Args:
            menu_name: 菜单名称
        """
        return "//div/span[text()='" + menu_name + "']"
