# coding:utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.BasePage import BasePage
from page.login_page import LoginPage

class TeacherClassList(BasePage):
    # “教学管理”
    teach_manage = (By.ID, 'teach_manage')

    # 我教的课-测试班级
    cls_button = (By.XPATH, "//div[@class='el-card__body'][1]")





    def teacher_class_check(self):
        driver = self.driver
        # 登录
        lp = LoginPage(self.driver)
        lp.login_first()

        # 等待并点击“教学管理”
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(TeacherClassList.teach_manage))
        self.click(TeacherClassList.teach_manage)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(TeacherClassList.cls_button))
        self.click(TeacherClassList.cls_button)



