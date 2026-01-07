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
        return "//iframe[@id='app-iframe-xxx']"

    def search_keyword_input(self):
        """搜索关键词输入框"""
        return "//input[@placeholder='课程代码 ｜ 课程名称']"

    def course_list_table(self):
        """课程列表表格"""
        return "//table[@class='course-list-table']"

    def course_name_link(self, course_name):
        """课程名称链接定位（根据课程名称）

        Args:
            course_name: 课程名称
        """
        return f"//a[contains(text(),'{course_name}')]"

    def view_button(self, course_code):
        """查看按钮定位（根据课程代码）

        Args:
            course_code: 课程代码
        """
        return f"//tr[contains(.,'{course_code}')]//button[contains(text(),'查看')]"

    def edit_button(self, course_code):
        """编辑按钮定位（根据课程代码）

        Args:
            course_code: 课程代码
        """
        return f"//tr[contains(.,'{course_code}')]//button[contains(text(),'编辑')]"
