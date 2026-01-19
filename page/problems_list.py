# coding:utf-8

"""
试卷库列表
"""
import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.BasePage import BasePage
from page.login_page import LoginPage

"""
题库：搜索习题，导出习题
"""


class ProblemList(BasePage):
    # “我的资源”
    my_resource_tab_loc = (By.ID, 'my_resource')
    # 题库tab
    my_problem_tab = (By.XPATH, "//span[contains(text(), '题库')]")
    # 导出习题按钮
    export_button_loc = (By.XPATH, "//div[contains(@class, 'btn-groups')]//a[contains(., '导出')]")
    # 搜索输入框
    search_input_loc = (By.XPATH, "//input[@placeholder='请输入题目内容或别名搜索']")
    # 搜索按钮
    search_button_loc = (By.XPATH, "//div[@class='el-input-group__append']//span[text()='搜索']")
    # 新建习题按钮
    add_button_loc = (By.XPATH, '//button[span[text()="新建习题"]]')
    # 弹窗-题型下拉框
    type_select_loc = (By.XPATH, "//div[label[contains(text(),'题型')]]//div[contains(@class,'el-select')]")
    # 弹窗-主观题选项
    subjective_option_loc = (By.XPATH, "//li[span[text()='主观题']]")
    # 弹窗-题干输入区域 (富文本编辑器)
    question_stem_loc = (By.XPATH, "//div[label[contains(text(),'题干')]]//div[@contenteditable='true']")
    # 弹窗-保存按钮
    save_button_loc = (By.XPATH, "//div[@class='el-dialog__footer']//button[span[text()='保存']]")
        
        
        


    # 页面动作
    def problem_check(self):
        driver = self.driver
        # 登录
        lp = LoginPage(self.driver)
        lp.login_first()

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'my_resource')))
        self.click(ProblemList.my_resource_tab_loc)
        
        # 等待并点击题库tab
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(ProblemList.my_problem_tab))
        self.click(ProblemList.my_problem_tab)
        
        # 执行导出操作
        self.click_export()



    # 搜索习题
    def search_problem(self, keyword):
        # 等待搜索框并输入文字
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(ProblemList.search_input_loc))
        self.send_keys(ProblemList.search_input_loc, keyword)
        # 点击搜索按钮
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProblemList.search_button_loc))
        self.click(ProblemList.search_button_loc)

        time.sleep(10)


    # 执行导出操作
    def click_export(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProblemList.export_button_loc))
        self.click(ProblemList.export_button_loc)


    def add_subjective_problem(self, content):
        # 1. 点击“新建习题”按钮
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProblemList.add_button_loc))
        self.click(ProblemList.add_button_loc)
        
        # 2. 点击题型下拉框
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProblemList.type_select_loc))
        self.click(ProblemList.type_select_loc)
        
        # 3. 选择“主观题”
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProblemList.subjective_option_loc))
        self.click(ProblemList.subjective_option_loc)
        
        # 4. 输入题干内容
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(ProblemList.question_stem_loc))
        self.send_keys(ProblemList.question_stem_loc, content)
        
        # 5. 点击保存按钮
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProblemList.save_button_loc))
        self.click(ProblemList.save_button_loc)





