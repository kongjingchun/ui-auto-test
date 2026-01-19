# coding:utf-8
import unittest
from base.base_util import BaseUtil
from page.teacher_class import TeacherClassList
from page.login_page import LoginPage

class TestTeacherClass(BaseUtil):
    def test_04(self):
        """ 我教的课"""
        # 先执行登录操作
        login_page = LoginPage(self.driver)
        login_result = login_page.login_first()
        assert login_result is True, "登录操作失败"
        
        # 执行教师班级检查
        mc = TeacherClassList(self.driver)
        mc.teacher_class_check()

if __name__ == '__main__':
    unittest.main()
