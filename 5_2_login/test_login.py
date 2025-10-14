# encoding: utf-8
# @File  : test_login.py
# @Author: kongjingchun
# @Date  : 2025/10/14/16:29
# @Desc  :
from time import sleep

from selenium.webdriver.common.by import By

from config.driver_config import DriverConfig

driver = DriverConfig().driver_config()
driver.get("http://120.53.230.254/login")
driver.find_element(By.XPATH, "//input[@placeholder='用户名']").send_keys("周杰伦")
sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='密码']").send_keys("123456")
sleep(2)
driver.find_element(By.XPATH, "//span[text()='登录']/parent::button").click()
sleep(2)
driver.quit()