# coding:utf-8
import unittest
from base.base_util import BaseUtil
from page.exam_list_copy import ExamList

class TestExamList(BaseUtil):
    def test_02(self):
        """ 试卷库页面"""
        el = ExamList(self.driver)
        el.exam_check()

if __name__ == '__main__':
    unittest.main()
