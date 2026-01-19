# coding:utf-8
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import re
from urllib import request as urllib_request
import cv2
from selenium.webdriver.common.action_chains import ActionChains
import random

class LoginPage(BasePage):

    """页面的元素"""

    #登录的首页
    login_page_first_loc = (By.XPATH, "//button[span[text()='登录']]")
    #切换登录方式
    login_method_loc= (By.XPATH, "//div[contains(@class,'login-switch')]")
    # 账号登录
    login_account_loc =(By.XPATH, "//div[contains(@class, 'text el-input')]//input[@placeholder='请输入账号']")
    password_loc = (By.XPATH, "//div[contains(@class, 'text el-input el-input--suffix')]//input[@placeholder='请输入密码']")
    # 记住密码
    remember_loc=(By.XPATH, "//label[@class='el-checkbox']")
    # 登录按钮
    login_btn_loc = (By.XPATH, "//button[span[text()='登 录']]")

    my_resource = (By.ID, 'my_resource')



    '''页面的动作'''

    def login_first(self,username="20210708",password="Abcd1234"):
        self.click(LoginPage.login_page_first_loc)
        self.click(LoginPage.login_method_loc)
        self.send_keys(LoginPage.login_account_loc,username)
        self.send_keys(LoginPage.password_loc,password)
        self.click(LoginPage.remember_loc)
        self.click(LoginPage.login_btn_loc)
        self.jy_slide()

    def jy_slide(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        iframe = wait.until(EC.presence_of_element_located((By.ID, "tcaptcha_iframe_dy")))
        driver.switch_to.frame(iframe)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'tcOperation')))

        max_retries = 3
        retries = 0
        distance = None

        while retries < max_retries and distance is None:

            try:
                # 获取验证码大图
                # print("当前是否在 iframe 里：", driver.execute_script("return window.self !== window.top"))
                # print(driver.page_source)

                def bg_has_image(driver):
                    try:
                        div = driver.find_element(By.ID, "slideBg")
                        return "background-image" in div.get_attribute("style")

                    except:
                        return False

                WebDriverWait(driver, 20).until(bg_has_image)

                # 获取背景图 URL
                bg_div = driver.find_element(By.ID, "slideBg")
                style = bg_div.get_attribute("style")
                match = re.search(r'background-image:\s*url\("([^"]+)"\)', style)
                if not match:
                    raise Exception("无法提取背景图 URL")
                bigImage_src = match.group(1)
                #print("背景图 URL:", bigImage_src)

                urllib_request.urlretrieve(bigImage_src, 'D:/bigImage.png')

                # 获取缺口位置
                distance = self.get_pos('D:/bigImage.png')

                if distance is None:

                    print("未找到缺口位置，尝试刷新验证码...")
                    # 点击刷新按钮（根据实际页面结构调整选择器）
                    refresh_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.ID, "reload"))  # 假设刷新按钮ID为e_reload
                    )
                    refresh_button.click()
                    retries += 1
                    time.sleep(2)  # 等待新验证码加载
                else:
                    break
            except Exception as e:
                print(f"验证码处理异常: {str(e)}")
                break

        if distance is None:
            raise Exception("验证码处理失败，已达最大重试次数")

        # 执行滑块操作
        smallImage = driver.find_element(By.XPATH, "//div[contains(@class,'tc-fg-item tc-slider-normal')]")
        distance = int(distance * 340 / 672 - smallImage.location['x'])

        ActionChains(driver).click_and_hold(smallImage).perform()
        moved = 0
        while moved < distance:
            x = random.randint(3, 8)
            moved += x
            ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
        ActionChains(driver).release().perform()

        # 切换回默认内容并继续后续操作
        driver.switch_to.default_content()
        time.sleep(3)  # 等待登录完成
        # 后续操作...

        """
        # 我的资源tab"// *[ @ id = 'app'] / div[2] / div[1]// div[1]// div[5]/div[1]"
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'my_resource')))
        my_resourse_tab = driver.find_element(By.ID, 'my_resource').click()

        # 找到试卷库tab
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), '试卷库')]")))
        my_exam = driver.find_element(By.XPATH, "//span[contains(text(), '试卷库')]").click()

        """

        # 选择试卷
        #定位到试卷
        #exam_publish = driver.find_element(By.XPATH, "//li[contains(@class, 'card_box') and .//div[contains(text(), '自动化测试试卷')]]//li[contains(text(), '发布')]").click()



    def get_pos(self, imageSrc):
        image = cv2.imread(imageSrc)
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        canny = cv2.Canny(blurred, 0, 10)
        contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            area = cv2.contourArea(contour)
            perimeter = cv2.arcLength(contour, True)
            if 5025 < area < 7225 and 300 < perimeter < 380:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.imwrite("D:/111.jpg", image)
                return x
        return None


    # 断言
    def get_except_result(self):
        return self.get_value(LoginPage.my_resource)

