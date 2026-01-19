# coding:utf-8
import unittest
from base.base_util import BaseUtil
from page.problems_list import ProblemList

class TestProblemList(BaseUtil):
    def test_03(self):
        """ 个人题库列表"""
        pl = ProblemList(self.driver)
        pl.problem_check()
        pl.search_problem("资源")

if __name__ == '__main__':
    unittest.main()
