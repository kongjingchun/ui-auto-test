# encoding: utf-8
# @File  : MyTeachingCoursesBase.py
# @Author:
# @Date  :
# @Desc  : 我教的课页面元素定位基类

class MyTeachingCoursesBase:
    """我教的课页面元素定位基类

    提供我教的课相关页面元素的XPath定位表达式
    """

    def my_teaching_courses_iframe(self):
        """我教的课iframe定位"""
        return "//iframe[@id='app-iframe-4003']"

    def course_search_input(self):
        """课程搜索输入框"""
        return "//input[@placeholder='搜索课程代码或名称']"

    def course_card_by_name(self, course_name):
        """根据课程名称定位课程卡片"""
        return "//div[@class='course-card' and contains(.,'" + course_name + "')]"