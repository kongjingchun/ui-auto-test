# coding:utf-8
import unittest
from base.base_util import BaseUtil
from page.teacher_class import TeacherClassList

class TestTeacherClass(BaseUtil):
    def test_04(self):
        """ 我教的课"""
        mc = TeacherClassList(self.driver)
        mc.teacher_class_check()

if __name__ == '__main__':
    unittest.main()
