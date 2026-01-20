# coding:utf-8

"""
试卷库列表
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from base.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExamListPage(BasePage):
    # "我的资源"
    my_resource_tab_loc = (By.ID, 'my_resource')
    # 试卷库tab
    my_exam_tab = (By.XPATH, "//span[contains(text(), '试卷库')]")
    # 试卷列表容器
    cards_list_loc = (By.XPATH, "//ul[contains(@class,'cards_list')]")
    # 第一个新版试卷卡片
    first_new_exam_card_loc = (By.XPATH, "//li[contains(@class,'card_box')][.//p[contains(@class,'card--type') and text()='新版试卷']][1]")
    # 发布按钮 - 多种定位方式
    publish_button = (By.XPATH, "//li[contains(@class,'card_box')][.//p[contains(@class,'card--type') and text()='新版试卷']][1]//li[contains(@class,'action-menu') and text()='发布']")
    # 备用定位方式1：通过actions_list定位
    publish_button_alt1 = (By.XPATH, "//li[contains(@class,'card_box')][.//p[text()='新版试卷']][1]//ul[contains(@class,'actions_list')]//li[text()='发布']")
    # 备用定位方式2：直接定位所有发布按钮中的第一个
    publish_button_alt2 = (By.XPATH, "(//li[contains(@class,'action-menu') and text()='发布'])[1]")





    # 页面动作
    def exam_check(self):
        driver = self.driver
        # 注意：登录操作应该在测试用例中完成，此方法只负责页面操作

        # 等待我的资源tab可见
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'my_resource')))
        self.click(ExamListPage.my_resource_tab_loc)

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), '试卷库')]")))
        self.click(ExamListPage.my_exam_tab)
        
        # 等待试卷列表加载完成
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(ExamListPage.cards_list_loc))
        time.sleep(2)  # 等待页面完全渲染
        
        # 点击发布按钮
        self.click_publish_button()
    
    def click_publish_button(self):
        """点击发布按钮，包含多种定位方式和错误处理"""
        driver = self.driver
        
        # 尝试多种定位方式
        publish_locators = [
            ExamListPage.publish_button,
            ExamListPage.publish_button_alt1,
            ExamListPage.publish_button_alt2
        ]
        
        publish_element = None
        for locator in publish_locators:
            try:
                # 等待元素可见并可点击
                publish_element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(locator)
                )
                # 滚动到元素可见
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", publish_element)
                time.sleep(0.5)  # 等待滚动完成
                break
            except Exception as e:
                print(f"定位方式失败: {locator}, 错误: {str(e)}")
                continue
        
        if publish_element is None:
            raise Exception("无法定位发布按钮，已尝试所有定位方式")
        
        # 尝试多种点击方式
        try:
            # 方式1：普通点击
            publish_element.click()
            print("使用普通点击方式成功")
        except Exception as e1:
            try:
                # 方式2：使用ActionChains点击
                ActionChains(driver).move_to_element(publish_element).click().perform()
                print("使用ActionChains点击方式成功")
            except Exception as e2:
                try:
                    # 方式3：使用JavaScript点击
                    driver.execute_script("arguments[0].click();", publish_element)
                    print("使用JavaScript点击方式成功")
                except Exception as e3:
                    raise Exception(f"所有点击方式都失败: 普通点击={str(e1)}, ActionChains={str(e2)}, JavaScript={str(e3)}")
        
        # 等待操作完成
        time.sleep(1)
