# encoding: utf-8
# @File  : teacher_class.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/21:17
# @Desc  : 教师班级列表页面对象类，封装教师班级相关的页面操作方法

from selenium.webdriver.common.by import By

from base.BasePage import BasePage
from logs.log import log


class TeacherClassList(BasePage):
    """教师班级列表页面类

    继承BasePage类，提供教师班级列表页面的元素操作方法
    符合Selenium官方Page Object Model设计模式
    """

    def __init__(self, driver):
        """初始化教师班级列表页面

        Args:
            driver: WebDriver实例
        """
        super().__init__(driver)

    # ==================== 定位器 ====================

    # 教学管理
    teach_manage = (By.ID, 'teach_manage')
    # 我教的课-测试班级
    cls_button = (By.XPATH, "//div[@class='el-card__body'][1]")

    # ==================== 页面操作方法 ====================

    def click_teach_manage(self):
        """点击教学管理

        Returns:
            bool: 点击操作结果，True表示成功
        """
        log.info("点击教学管理")
        try:
            self.click(self.teach_manage, timeout=20)
            return True
        except Exception as e:
            log.error(f"点击教学管理失败：{str(e)}")
            return False

    def click_class_button(self):
        """点击测试班级

        Returns:
            bool: 点击操作结果，True表示成功
        """
        log.info("点击测试班级")
        try:
            self.click(self.cls_button, timeout=20)
            return True
        except Exception as e:
            log.error(f"点击测试班级失败：{str(e)}")
            return False

    def teacher_class_check(self):
        """检查教师班级（导航操作）

        注意：登录操作应该在测试用例中完成，此方法只负责页面操作。

        Returns:
            bool: 操作结果，True表示成功
        """
        log.info("执行教师班级检查")
        try:
            # 点击教学管理
            result = self.click_teach_manage()
            if not result:
                return False

            # 点击测试班级
            result = self.click_class_button()
            return result
        except Exception as e:
            log.error(f"教师班级检查失败：{str(e)}")
            return False
