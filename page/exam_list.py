# encoding: utf-8
# @File  : exam_list.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/21:17
# @Desc  : 试卷库列表页面对象类，封装试卷库相关的页面操作方法

from selenium.webdriver.common.by import By

from base.BasePage import BasePage
from logs.log import log


class ExamList(BasePage):
    """试卷库列表页面类

    继承BasePage类，提供试卷库列表页面的元素操作方法
    符合Selenium官方Page Object Model设计模式
    """

    def __init__(self, driver):
        """初始化试卷库列表页面

        Args:
            driver: WebDriver实例
        """
        super().__init__(driver)

    # ==================== 定位器 ====================

    # 我的资源
    my_resource_tab_loc = (By.ID, 'my_resource')
    # 试卷库tab
    my_exam_tab = (By.XPATH, "//span[contains(text(), '试卷库')]")
    # 发布按钮
    publish_button = (By.XPATH,
                      "//li[contains(@class,'card_box')][.//p[contains(@class,'card--type') and text()='新版试卷']]//li[contains(@class,'action-menu') and text()='发布']")
    # iframe定位器
    iframe_locator = (By.XPATH, "//iframe[@data-v-f385c0c2]")

    # ==================== 页面操作方法 ====================

    def click_my_resource_tab(self):
        """点击我的资源tab

        Returns:
            bool: 点击操作结果，True表示成功
        """
        log.info("点击我的资源tab")
        try:
            self.click(self.my_resource_tab_loc, timeout=20)
            return True
        except Exception as e:
            log.error(f"点击我的资源tab失败：{str(e)}")
            return False

    def click_exam_tab(self):
        """点击试卷库tab

        Returns:
            bool: 点击操作结果，True表示成功
        """
        log.info("点击试卷库tab")
        try:
            self.click(self.my_exam_tab, timeout=20)
            return True
        except Exception as e:
            log.error(f"点击试卷库tab失败：{str(e)}")
            return False

    def click_publish_button(self):
        """点击发布按钮（需要在iframe中操作）

        Returns:
            bool: 点击操作结果，True表示成功
        """
        log.info("点击发布按钮")
        try:
            # 切换到iframe
            self.switch_to_iframe(self.iframe_locator, timeout=10)

            # 点击发布按钮
            self.click(self.publish_button, timeout=20)

            # 切换回默认内容
            self.switch_out_iframe()
            return True
        except Exception as e:
            log.error(f"点击发布按钮失败：{str(e)}")
            # 确保切换回默认内容
            try:
                self.switch_out_iframe()
            except:
                pass
            return False

    def exam_check(self):
        """检查试卷库（导航操作）

        注意：登录操作应该在测试用例中完成，此方法只负责页面操作。

        Returns:
            bool: 操作结果，True表示成功
        """
        log.info("执行试卷库检查")
        try:
            # 点击我的资源tab
            result = self.click_my_resource_tab()
            if not result:
                return False

            # 点击试卷库tab
            result = self.click_exam_tab()
            if not result:
                return False

            # 点击发布按钮
            result = self.click_publish_button()
            return result
        except Exception as e:
            log.error(f"试卷库检查失败：{str(e)}")
            return False
