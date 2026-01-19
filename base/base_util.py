# encoding: utf-8
import unittest
from config.driver_config import DriverConfig

class BaseUtil(unittest.TestCase):
    """
    测试用例基类，提供 WebDriver 的初始化和清理
    """
    def setUp(self):
        self.driver = DriverConfig.driver_config()

    def tearDown(self):
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()
