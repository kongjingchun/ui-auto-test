# coding:utf-8

"""
试卷库列表
"""
from selenium.webdriver.common.by import By

from base.BasePage import BasePage
from page.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExamList(BasePage):
    # “我的资源”
    my_resource_tab_loc = (By.ID, 'my_resource')
    # 试卷库tab
    my_exam_tab = (By.XPATH, "//span[contains(text(), '试卷库')]")
    # 发布按钮
    publish_button = (By.XPATH,
                      "//li[contains(@class,'card_box')][.//p[contains(@class,'card--type') and text()='新版试卷']]//li[contains(@class,'action-menu') and text()='发布']")




    # 页面动作
    def exam_check(self):
        driver = self.driver
        # 登录
        lp = LoginPage(self.driver)
        lp.login_first()

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'my_resource')))
        self.click(ExamList.my_resource_tab_loc)

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), '试卷库')]")))
        self.click(ExamList.my_exam_tab)

        driver = self.driver
        wait = WebDriverWait(driver, 10)
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@data-v-f385c0c2]")))
        driver.switch_to.frame(iframe)

        # 等待第一个“发布”按钮并点击
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(ExamList.publish_button))
        self.click(ExamList.publish_button)
