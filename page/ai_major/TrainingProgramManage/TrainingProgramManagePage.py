# encoding: utf-8
# @File  : TrainingProgramManagePage.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 培养方案管理页面对象类，封装培养方案管理相关的页面操作方法

from time import sleep

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.ai_major.TrainingProgramManage.TrainingProgramManageBase import TrainingProgramManageBase
from logs.log import log


class TrainingProgramManagePage(TrainingProgramManageBase, ObjectMap):
    """培养方案管理页面类

    继承TrainingProgramManageBase和ObjectMap类，提供培养方案管理页面的元素操作方法
    """

    def switch_into_training_program_manage_iframe(self, driver):
        """切换到培养方案管理iframe

        Args:
            driver: WebDriver实例

        Returns:
            切换操作结果
        """
        xpath = self.training_program_manage_iframe()
        log.info(f"切换到培养方案管理iframe，xpath定位为：{xpath}")
        return self.switch_into_iframe(driver, By.XPATH, xpath)

    def switch_out_training_program_manage_iframe(self, driver):
        """从培养方案管理iframe切出

        Args:
            driver: WebDriver实例

        Returns:
            切换操作结果
        """
        log.info("从培养方案管理iframe切出")
        return self.switch_out_iframe(driver)

    def input_search_keyword(self, driver, keyword):
        """输入搜索关键词

        Args:
            driver: WebDriver实例
            keyword: 搜索关键词

        Returns:
            输入操作结果
        """
        xpath = self.search_keyword_input()
        log.info(f"输入搜索关键词：{keyword}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, keyword)

    def click_import_training_program_button(self, driver):
        """点击导入培养方案按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.import_training_program_button()
        log.info(f"点击导入培养方案按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_training_program_button(self, driver):
        """点击新建培养方案按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_button()
        log.info(f"点击新建培养方案按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def input_new_training_program_input(self, driver, input_name, value):
        """输入新建培养方案信息

        Args:
            driver: WebDriver实例
            input_name: 输入框名称（如：'方案名称'、'学分要求'、'版本年份'）
            value: 输入的值

        Returns:
            输入操作结果
        """
        xpath = self.new_training_program_input(input_name)
        if xpath is None:
            log.error(f"未找到输入框：{input_name}")
            return False
        log.info(f"输入新建培养方案信息：{input_name}为：{value}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, value)

    def click_new_training_program_major_dropdown(self, driver):
        """点击关联专业下拉框

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_major_dropdown()
        log.info(f"点击关联专业下拉框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_training_program_major_dropdown_option(self, driver, major_name):
        """点击关联专业下拉框选项

        Args:
            driver: WebDriver实例
            major_name: 专业名称

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_major_dropdown_option(major_name)
        log.info(f"点击关联专业下拉框选项：{major_name}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)
        # 点击后等待下拉菜单关闭
        sleep(0.5)
        return result

    def click_new_training_program_type_dropdown(self, driver):
        """点击培养类型下拉框

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_type_dropdown()
        log.info(f"点击培养类型下拉框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_training_program_type_dropdown_option(self, driver, type_name):
        """点击培养类型下拉框选项

        Args:
            driver: WebDriver实例
            type_name: 培养类型名称

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_type_dropdown_option(type_name)
        log.info(f"点击培养类型下拉框选项：{type_name}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)
        # 点击后等待下拉菜单关闭
        sleep(0.5)
        return result

    def click_new_training_program_level_dropdown(self, driver):
        """点击培养层次下拉框

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_level_dropdown()
        log.info(f"点击培养层次下拉框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_training_program_level_dropdown_option(self, driver, level_name):
        """点击培养层次下拉框选项

        Args:
            driver: WebDriver实例
            level_name: 培养层次名称

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_level_dropdown_option(level_name)
        log.info(f"点击培养层次下拉框选项：{level_name}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)
        # 点击后等待下拉菜单关闭
        sleep(0.5)
        return result

    def click_new_training_program_duration_dropdown(self, driver):
        """点击学制下拉框

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_duration_dropdown()
        log.info(f"点击学制下拉框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_training_program_duration_dropdown_option(self, driver, duration):
        """点击学制下拉框选项

        Args:
            driver: WebDriver实例
            duration: 学制

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_duration_dropdown_option(duration)
        log.info(f"点击学制下拉框选项：{duration}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)
        # 点击后等待下拉菜单关闭
        sleep(0.5)
        return result

    def click_new_training_program_degree_dropdown(self, driver):
        """点击授予学位下拉框

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_degree_dropdown()
        log.info(f"点击授予学位下拉框，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_training_program_degree_dropdown_option(self, driver, degree_name):
        """点击授予学位下拉框选项

        Args:
            driver: WebDriver实例
            degree_name: 授予学位名称

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_degree_dropdown_option(degree_name)
        log.info(f"点击授予学位下拉框选项：{degree_name}，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)
        # 点击后等待下拉菜单关闭
        sleep(0.5)
        return result

    def click_new_training_program_credit_increase_button(self, driver):
        """点击学分要求增加按钮（+按钮）

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_credit_increase_button()
        log.info(f"点击学分要求增加按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_training_program_credit_decrease_button(self, driver):
        """点击学分要求减少按钮（-按钮）

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_credit_decrease_button()
        log.info(f"点击学分要求减少按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_training_program_year_increase_button(self, driver):
        """点击版本年份增加按钮（+按钮）

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_year_increase_button()
        log.info(f"点击版本年份增加按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_training_program_year_decrease_button(self, driver):
        """点击版本年份减少按钮（-按钮）

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_year_decrease_button()
        log.info(f"点击版本年份减少按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_training_program_cancel_button(self, driver):
        """点击新建培养方案取消按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_cancel_button()
        log.info(f"点击新建培养方案取消按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def click_new_training_program_create_button(self, driver):
        """点击新建培养方案创建按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.new_training_program_create_button()
        log.info(f"点击新建培养方案创建按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath)

    def is_create_success_alert_display(self, driver):
        """查看创建成功提示框是否出现

        Args:
            driver: WebDriver实例

        Returns:
            bool: True表示创建成功提示框出现，False表示未出现
        """
        xpath = self.create_success_alert()
        log.info(f"查看创建成功提示框是否出现，xpath定位为：{xpath}")
        return self.element_is_display(driver, By.XPATH, xpath)

    def click_revision_button_by_program_name(self, driver, program_name):
        """根据方案名称点击修订按钮

        Args:
            driver: WebDriver实例
            program_name: 培养方案名称

        Returns:
            点击操作结果
        """
        # 切换到iframe
        self.switch_into_training_program_manage_iframe(driver)

        # 根据方案名称点击修订按钮
        xpath = self.training_program_revision_button(program_name)
        log.info(f"点击方案名称'{program_name}'后的修订按钮，xpath定位为：{xpath}")
        result = self.element_click(driver, By.XPATH, xpath, timeout=15)

        # 切出iframe
        self.switch_out_training_program_manage_iframe(driver)

        log.info(f"点击方案名称'{program_name}'后的修订按钮结果：{result}")
        return result

    def click_more_button_by_program_name(self, driver, program_name):
        """根据方案名称点击更多按钮

        Args:
            driver: WebDriver实例
            program_name: 培养方案名称

        Returns:
            点击操作结果
        """
        # 根据方案名称点击更多按钮
        xpath = self.training_program_more_button(program_name)
        log.info(f"点击方案名称'{program_name}'后的更多按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

    def click_edit_property_button_by_program_name(self, driver, program_name):
        """根据方案名称点击编辑属性按钮

        先点击更多按钮，然后在下拉菜单中点击编辑属性按钮
        Args:
            driver: WebDriver实例
            program_name: 培养方案名称

        Returns:
            点击操作结果
        """
        edit_property_xpath = self.training_program_edit_property_button()
        log.info(f"点击编辑属性按钮，xpath定位为：{edit_property_xpath}")
        return self.element_click(driver, By.XPATH, edit_property_xpath, timeout=15)

    def click_delete_training_program_button(self, driver):
        """点击删除培养方案按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.delete_training_program_button()
        log.info(f"点击删除培养方案按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

    def click_delete_confirm_button(self, driver):
        """点击删除确认按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.delete_confirm_button()
        log.info(f"点击删除确认按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=15)

    def is_delete_success_alert_display(self, driver):
        """断言删除成功提示框是否出现

        Args:
            driver: WebDriver实例

        Returns:
            bool: True表示删除成功提示框出现，False表示未出现
        """
        xpath = self.delete_success_alert()
        log.info(f"断言删除成功提示框是否出现，xpath定位为：{xpath}")
        return self.element_is_display(driver, By.XPATH, xpath)

    def create_training_program(self, driver, training_program_info):
        """创建培养方案

        Args:
            driver: WebDriver实例
            training_program_info: 培养方案信息

        Returns:
            bool: True表示创建成功，False表示创建失败
        """
        # 切换到iframe
        self.switch_into_training_program_manage_iframe(driver)

        # 点击新建培养方案按钮
        self.click_new_training_program_button(driver)
        sleep(0.5)

        # 从上到下设置新建信息
        # 1. 方案名称
        self.input_new_training_program_input(driver, "方案名称", training_program_info['方案名称'])

        # 2. 所属院系（不需要更改默认，跳过）

        # 3. 关联专业
        self.click_new_training_program_major_dropdown(driver)
        self.click_new_training_program_major_dropdown_option(driver, training_program_info['关联专业'])

        # 4. 培养类型
        self.click_new_training_program_type_dropdown(driver)
        self.click_new_training_program_type_dropdown_option(driver, training_program_info['培养类型'])

        # 5. 培养层次
        self.click_new_training_program_level_dropdown(driver)
        self.click_new_training_program_level_dropdown_option(driver, training_program_info['培养层次'])

        # 6. 学制
        self.click_new_training_program_duration_dropdown(driver)
        self.click_new_training_program_duration_dropdown_option(driver, training_program_info['学制'])

        # 7. 学分要求（不需要更改默认，跳过）

        # 8. 授予学位
        self.click_new_training_program_degree_dropdown(driver)
        self.click_new_training_program_degree_dropdown_option(driver, training_program_info['授予学位'])

        # 9. 版本年份（不需要更改默认，跳过）

        # 点击创建按钮
        self.click_new_training_program_create_button(driver)
        sleep(1)

        # 断言创建成功提示框是否出现
        result = self.is_create_success_alert_display(driver)

        # 切出iframe
        self.switch_out_training_program_manage_iframe(driver)

        log.info(f"创建培养方案结果：{result}")
        return result

    def delete_training_program_by_program_name(self, driver, program_name):
        """根据方案名称删除培养方案

        Args:
            driver: WebDriver实例
            program_name: 培养方案名称

        Returns:
            bool: True表示删除成功，False表示删除失败
        """
        # 切换到iframe
        self.switch_into_training_program_manage_iframe(driver)
        # 输入搜索关键词
        self.input_search_keyword(driver, program_name)
        # 点击更多按钮
        self.click_more_button_by_program_name(driver, program_name)
        # 点击编辑属性按钮
        self.click_edit_property_button_by_program_name(driver, program_name)
        # 根据方案名称点击删除按钮
        self.click_delete_training_program_button(driver)
        # 点击删除确认按钮
        self.click_delete_confirm_button(driver)
        # 断言删除成功提示框是否出现
        result = self.is_delete_success_alert_display(driver)
        # 切出iframe
        self.switch_out_training_program_manage_iframe(driver)
        log.info(f"删除培养方案结果：{result}")
        return result
