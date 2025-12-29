# encoding: utf-8
# @File  : test_002_initialize_dept_major.py.py
# @Author: 孔敬淳
# @Date  : 2025/12/29/16:34
# @Desc  :
import allure

from common.yaml_config import GetConf


class TestInitializeDeptMajor:
    """初始学校院系、专业等流程"""

    @allure.story("初始化学校")
    def test_001_initialize_dept_major(self, driver):
        """
        初始学校院系、专业等流程
        :param driver: WebDriver实例
        :return: None
        """
        GetConf().g