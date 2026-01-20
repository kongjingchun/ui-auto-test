# coding:utf-8
import unittest
from base.base_util import BaseUtil
from page.exam_list import ExamListPage
from page.login_page import LoginPage

class TestExamList(BaseUtil):
    def test_02(self):
        """ 试卷库页面"""
        # 先执行登录操作
        login_page = LoginPage(self.driver)
        login_result = login_page.login_first()
        assert login_result is True, "登录操作失败"
        
        # 执行试卷库检查
        el = ExamListPage(self.driver)
        el.exam_check()

if __name__ == '__main__':
    unittest.main()
