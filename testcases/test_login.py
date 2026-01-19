# coding:utf-8

import unittest

import pytest
from ddt import ddt, data, unpack
from selenium import webdriver

from base.base_util import BaseUtil
# from common.excel_util import ExcelUtil  # 文件不存在，暂时注释
from page.login_page import LoginPage

#print(">>> DEBUG: loading", __file__)

@ddt
class TestLogin(BaseUtil):

    """账密登录"""

    #@data(*ExcelUtil().read_excel())
    #@unpack
    #def test_01_login(self,index,username,password):
    def test_01_login(self):
    
        #print(index,username,password)

        lp = LoginPage(self.driver)
        lp.login_first()
         #断言(用例1是正例)
        #if index ==1:
        self.assertEqual(lp.get_except_result(),'我的资源')


    """
    @pytest.mark.parametrize("datainfo",ExcelUtil().read_excel())
    def test_01_login(self,datainfo):
        print(datainfo)
        """
