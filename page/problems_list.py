# encoding: utf-8
# @File  : problems_list.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/21:17
# @Desc  : 题库列表页面对象类，封装题库相关的页面操作方法

import time
from selenium.webdriver.common.by import By

from base.BasePage import BasePage
from logs.log import log


class ProblemList(BasePage):
    """题库列表页面类

    继承BasePage类，提供题库列表页面的元素操作方法
    符合Selenium官方Page Object Model设计模式
    """

    def __init__(self, driver):
        """初始化题库列表页面

        Args:
            driver: WebDriver实例
        """
        super().__init__(driver)

    # ==================== 定位器 ====================

    # 我的资源
    my_resource_tab_loc = (By.ID, 'my_resource')
    # 题库tab
    my_problem_tab = (By.XPATH, "//span[contains(text(), '题库')]")
    # 导出习题按钮
    export_button_loc = (By.XPATH, "//div[contains(@class, 'btn-groups')]//a[contains(., '导出')]")
    # 搜索输入框
    search_input_loc = (By.XPATH, "//input[@placeholder='请输入题目内容或别名搜索']")
    # 搜索按钮
    search_button_loc = (By.XPATH, "//div[@class='el-input-group__append']//span[text()='搜索']")
    # 弹窗-题型下拉框
    type_select_loc = (By.XPATH, "//div[label[contains(text(),'题型')]]//div[contains(@class,'el-select')]")
    # 弹窗-主观题选项
    subjective_option_loc = (By.XPATH, "//li[span[text()='主观题']]")
    # 弹窗-题干输入区域 (富文本编辑器)
    question_stem_loc = (By.XPATH, "//div[label[contains(text(),'题干')]]//div[@contenteditable='true']")
    # 弹窗-保存按钮
    save_button_loc = (By.XPATH, "//div[@class='el-dialog__footer']//button[span[text()='保存']]")
    # 新建习题按钮
    add_button_loc = (By.XPATH, "//span[contains(.,'新建习题')]/parent::button")

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

    def click_problem_tab(self):
        """点击题库tab

        Returns:
            bool: 点击操作结果，True表示成功
        """
        log.info("点击题库tab")
        try:
            self.click(self.my_problem_tab, timeout=20)
            return True
        except Exception as e:
            log.error(f"点击题库tab失败：{str(e)}")
            return False

    def click_export(self):
        """点击导出按钮

        Returns:
            bool: 点击操作结果，True表示成功
        """
        log.info("点击导出按钮")
        try:
            self.click(self.export_button_loc, timeout=20)
            return True
        except Exception as e:
            log.error(f"点击导出按钮失败：{str(e)}")
            return False

    def search_problem(self, keyword):
        """搜索习题

        Args:
            keyword: 搜索关键词

        Returns:
            bool: 搜索操作结果，True表示成功
        """
        log.info(f"搜索习题，关键词：{keyword}")
        try:
            # 等待搜索框并输入文字
            self.input_text(self.search_input_loc, keyword, timeout=20)
            # 点击搜索按钮
            self.click(self.search_button_loc, timeout=20)
            time.sleep(10)  # 等待搜索结果加载
            return True
        except Exception as e:
            log.error(f"搜索习题失败：{str(e)}")
            return False

    def click_add_button(self):
        """点击新建习题按钮

        Returns:
            bool: 点击操作结果，True表示成功
        """
        log.info("点击新建习题按钮")
        try:
            self.click(self.add_button_loc, timeout=20)
            return True
        except Exception as e:
            log.error(f"点击新建习题按钮失败：{str(e)}")
            return False

    def add_subjective_problem(self, content):
        """添加主观题

        Args:
            content: 题干内容

        Returns:
            bool: 添加操作结果，True表示成功
        """
        log.info(f"添加主观题，内容：{content}")
        try:
            # 1. 点击"新建习题"按钮
            self.click(self.add_button_loc, timeout=20)

            # 2. 点击题型下拉框
            self.click(self.type_select_loc, timeout=20)

            # 3. 选择"主观题"
            self.click(self.subjective_option_loc, timeout=20)

            # 4. 输入题干内容
            self.input_text(self.question_stem_loc, content, timeout=20)

            # 5. 点击保存按钮
            self.click(self.save_button_loc, timeout=20)
            return True
        except Exception as e:
            log.error(f"添加主观题失败：{str(e)}")
            return False

    def problem_check(self):
        """检查题库（导航操作）

        注意：登录操作应该在测试用例中完成，此方法只负责页面操作。

        Returns:
            bool: 操作结果，True表示成功
        """
        log.info("执行题库检查")
        try:
            # 点击我的资源tab
            result = self.click_my_resource_tab()
            if not result:
                return False

            # 点击题库tab
            result = self.click_problem_tab()
            if not result:
                return False

            # 执行导出操作
            result = self.click_export()
            return result
        except Exception as e:
            log.error(f"题库检查失败：{str(e)}")
            return False
