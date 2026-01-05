# encoding: utf-8
# @File  : TrainingProgramRevisionPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 培养方案修订页面对象类，封装培养方案修订相关的页面操作方法

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.ai_major.TrainingProgramManageBase import TrainingProgramManageBase
from base.ai_major.TrainingProgramRevisionBase import TrainingProgramRevisionBase
from logs.log import log


class TrainingProgramRevisionPage(TrainingProgramRevisionBase, TrainingProgramManageBase, ObjectMap):
    """培养方案修订页面类

    继承TrainingProgramRevisionBase和ObjectMap类，提供培养方案修订页面的元素操作方法
    包含5个子页面：专业信息、培养目标、毕业要求、课程体系、课程支撑
    """

    # ==================== 通用操作方法 ====================
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

    def click_tab(self, driver, tab_name):
        """点击标签页

        Args:
            driver: WebDriver实例
            tab_name: 标签页名称，如 '专业信息'、'培养目标'、'毕业要求'、'目标支撑'、'课程体系'、'课程支撑'

        Returns:
            点击操作结果
        """
        xpath = self.revision_tab(tab_name)
        log.info(f"点击标签页：{tab_name}，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_save_button(self, driver):
        """点击保存按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.save_button()
        log.info(f"点击保存按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_cancel_button(self, driver):
        """点击取消按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.cancel_button()
        log.info(f"点击取消按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def is_save_success_alert_display(self, driver, content="保存成功"):
        """根据内容判断保存成功提示框是否出现

        Args:
            driver: WebDriver实例
            content: 提示框内容文本，默认为"保存成功"

        Returns:
            bool: True表示保存成功提示框出现，False表示未出现
        """
        xpath = self.save_success_alert(content)
        log.info(f"查看保存成功提示框是否出现，xpath定位为：{xpath}")
        return self.element_is_display(driver, By.XPATH, xpath)

    # ==================== 专业信息页面操作方法 ====================
    def input_major_description(self, driver, description):
        """输入专业描述

        Args:
            driver: WebDriver实例
            description: 专业描述内容

        Returns:
            输入操作结果
        """
        xpath = self.major_description_input()
        log.info(f"输入专业描述：{description}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, description)

    def update_major_info(self, driver, description=None):
        """更新专业信息

        Args:
            driver: WebDriver实例
            description: 专业描述内容

        Returns:
            bool: True表示更新成功，False表示更新失败
        """
        # 切换到iframe
        self.switch_into_training_program_manage_iframe(driver)

        # 点击专业信息标签页
        self.click_tab(driver, "专业信息")
        # 输入专业描述
        self.input_major_description(driver, description)
        # 点击保存按钮
        self.click_save_button(driver)
        # 断言保存成功提示框是否出现
        result = self.is_save_success_alert_display(driver)

        # 切出iframe
        self.switch_out_training_program_manage_iframe(driver)

        log.info(f"更新专业信息结果：{result}")
        return result

    # ==================== 培养目标页面操作方法 ====================
    def input_training_objective_overview(self, driver, overview):
        """输入培养目标概述

        Args:
            driver: WebDriver实例
            overview: 培养目标概述内容

        Returns:
            输入操作结果
        """
        xpath = self.training_objective_overview_textarea()
        log.info(f"输入培养目标概述：{overview}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, overview)

    def click_add_training_objective_button(self, driver):
        """点击添加目标按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.add_training_objective_button()
        log.info(f"点击添加目标按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def input_training_objective_description(self, driver, description):
        """输入培养目标描述

        Args:
            driver: WebDriver实例
            description: 培养目标描述内容

        Returns:
            输入操作结果
        """
        xpath = self.training_objective_description_textarea()
        log.info(f"输入培养目标描述：{description}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, description)

    def click_training_objective_save_button(self, driver):
        """点击培养目标保存按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.training_objective_save_button()
        log.info(f"点击培养目标保存按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def update_training_objective(self, driver, overview=None, description=None):
        """更新培养目标

        Args:
            driver: WebDriver实例
            overview: 培养目标概述内容
            description: 培养目标描述内容

        Returns:
            bool: True表示更新成功，False表示更新失败
        """
        # 切换到iframe
        self.switch_into_training_program_manage_iframe(driver)

        # 点击培养目标标签页
        self.click_tab(driver, "培养目标")
        # 输入培养目标概述
        self.input_training_objective_overview(driver, overview)
        # 点击保存按钮
        self.click_save_button(driver)
        # 点击添加目标按钮
        self.click_add_training_objective_button(driver)
        # 输入培养目标描述
        self.input_training_objective_description(driver, description)
        # 点击保存培养目标按钮
        self.click_training_objective_save_button(driver)
        # 点击保存按钮
        self.click_save_button(driver)
        # 断言保存成功提示框是否出现
        result = self.is_save_success_alert_display(driver)

        # 切出iframe
        self.switch_out_training_program_manage_iframe(driver)

        log.info(f"更新培养目标结果：{result}")
        return result

    # ==================== 毕业要求页面操作方法 ====================
    def input_graduation_requirement_description(self, driver, description):
        """输入毕业要求概述

        Args:
            driver: WebDriver实例
            description: 毕业要求概述内容

        Returns:
            输入操作结果
        """
        xpath = self.graduation_requirement_description_textarea()
        log.info(f"输入毕业要求概述：{description}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, description)

    def click_add_indicator_point_button(self, driver):
        """点击添加指标点按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.add_indicator_point_button()
        log.info(f"点击添加指标点按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def input_indicator_point_name(self, driver, name, indicator_index=1):
        """输入指标点名称

        Args:
            driver: WebDriver实例
            name: 指标点名称
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）

        Returns:
            输入操作结果
        """
        xpath = self.indicator_point_name_input(indicator_index)
        log.info(f"输入指标点名称（索引：{indicator_index}）：{name}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, name)

    def input_indicator_point_description(self, driver, description, indicator_index=1):
        """输入指标点描述

        Args:
            driver: WebDriver实例
            description: 指标点描述内容
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）

        Returns:
            输入操作结果
        """
        xpath = self.indicator_point_description_textarea(indicator_index)
        log.info(f"输入指标点描述（索引：{indicator_index}）：{description}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, description)

    def click_expand_button(self, driver, indicator_index=1):
        """点击展开按钮

        Args:
            driver: WebDriver实例
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）

        Returns:
            点击操作结果
        """
        xpath = self.expand_button(indicator_index)
        log.info(f"点击展开按钮（指标点索引：{indicator_index}），xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_add_decomposed_indicator_point_button(self, driver, indicator_index=1):
        """点击添加分解指标点按钮

        Args:
            driver: WebDriver实例
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）

        Returns:
            点击操作结果
        """
        xpath = self.add_decomposed_indicator_point_button(indicator_index)
        log.info(f"点击添加分解指标点按钮（指标点索引：{indicator_index}），xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def input_decomposed_indicator_point_name(self, driver, name, indicator_index=1, decomposed_index=1):
        """输入分解指标点名称

        Args:
            driver: WebDriver实例
            name: 分解指标点名称
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）
            decomposed_index: 分解指标点序号，从1开始，默认为1（第1个分解指标点）

        Returns:
            输入操作结果
        """
        xpath = self.decomposed_indicator_point_name_input(indicator_index, decomposed_index)
        log.info(f"输入分解指标点名称（指标点索引：{indicator_index}，分解指标点索引：{decomposed_index}）：{name}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, name)

    def input_decomposed_indicator_point_description(self, driver, description, indicator_index=1, decomposed_index=1):
        """输入分解指标点描述

        Args:
            driver: WebDriver实例
            description: 分解指标点描述内容
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）
            decomposed_index: 分解指标点序号，从1开始，默认为1（第1个分解指标点）

        Returns:
            输入操作结果
        """
        xpath = self.decomposed_indicator_point_description_textarea(indicator_index, decomposed_index)
        log.info(f"输入分解指标点描述（指标点索引：{indicator_index}，分解指标点索引：{decomposed_index}）：{description}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, description)

    def update_graduation_requirement(self, driver, description=None, indicator_index=1, indicator_name=None, indicator_description=None, decomposed_indicator_index=1, decomposed_indicator_name=None, decomposed_indicator_description=None):
        """更新毕业要求

        Args:
            driver: WebDriver实例
            description: 毕业要求概述内容
            indicator_index: 指标点序号，从1开始，默认为1（第1个指标点）
            indicator_name: 指标点名称
            indicator_description: 指标点描述内容
            decomposed_indicator_index: 分解指标点序号，从1开始，默认为1（第1个分解指标点）
            decomposed_indicator_name: 分解指标点名称
            decomposed_indicator_description: 分解指标点描述内容

        Returns:
            bool: True表示更新成功，False表示更新失败
        """
        # 切换到iframe
        self.switch_into_training_program_manage_iframe(driver)

        # 点击毕业要求标签页
        self.click_tab(driver, "毕业要求")
        # 输入毕业要求概述
        self.input_graduation_requirement_description(driver, description)
        # 点击添加指标点按钮
        self.click_add_indicator_point_button(driver)
        # 输入指标点名称
        self.input_indicator_point_name(driver, indicator_name, indicator_index)
        # 输入指标点描述
        self.input_indicator_point_description(driver, indicator_description, indicator_index)
        # 点击展开按钮
        self.click_expand_button(driver, indicator_index)
        # 点击添加分解指标点按钮
        self.click_add_decomposed_indicator_point_button(driver, indicator_index)
        # 输入分解指标点名称
        self.input_decomposed_indicator_point_name(driver, decomposed_indicator_name, indicator_index, decomposed_indicator_index)
        # 输入分解指标点描述
        self.input_decomposed_indicator_point_description(driver, decomposed_indicator_description, indicator_index, decomposed_indicator_index)
        # 点击保存按钮
        self.click_save_button(driver)
        # 断言保存成功提示框是否出现
        result = self.is_save_success_alert_display(driver)

        # 切出iframe
        self.switch_out_training_program_manage_iframe(driver)

        log.info(f"更新毕业要求结果：{result}")
        return result

    # ==================== 目标支撑页面操作方法 ====================
    def click_target_support_select_button(self, driver, index=1):
        """点击目标支撑选择按钮

        Args:
            driver: WebDriver实例
            index: 选择按钮序号，从1开始，默认为1（第1个选择按钮）

        Returns:
            点击操作结果
        """
        xpath = self.target_support_select_button(index)
        log.info(f"点击目标支撑选择按钮（索引：{index}），xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_target_support_level_option(self, driver, level="高支撑"):
        """点击目标支撑等级选项

        Args:
            driver: WebDriver实例
            level: 支撑等级，有高支撑、中支撑、低支撑、无支撑4个选项

        Returns:
            点击操作结果
        """
        xpath = self.target_support_level_option(level)
        log.info(f"点击目标支撑等级选项：{level}，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def update_target_support(self, driver, index=1, level="高支撑"):
        """更新目标支撑

        Args:
            driver: WebDriver实例
            index: 选择按钮序号，从1开始，默认为1（第1个选择按钮）
            level: 支撑等级，有高支撑、中支撑、低支撑、无支撑4个选项

        Returns:
            bool: True表示更新成功，False表示更新失败
        """
        # 切换到iframe
        self.switch_into_training_program_manage_iframe(driver)

        # 点击目标支撑标签页
        self.click_tab(driver, "目标支撑")
        # 点击目标支撑选择按钮
        self.click_target_support_select_button(driver, index)
        # 点击目标支撑等级选项
        self.click_target_support_level_option(driver, level)
        # 点击保存按钮
        self.click_save_button(driver)
        # 断言保存成功提示框是否出现
        result = self.is_save_success_alert_display(driver)

        # 切出iframe
        self.switch_out_training_program_manage_iframe(driver)

        log.info(f"更新目标支撑结果：{result}")
        return result
    # ==================== 课程体系页面操作方法 ====================

    def click_add_course_button(self, driver):
        """点击添加课程按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.add_course_button()
        log.info(f"点击添加课程按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def input_course_search(self, driver, search_keyword):
        """输入课程搜索关键词（课程名称或代码）

        Args:
            driver: WebDriver实例
            search_keyword: 搜索关键词（课程名称或代码）

        Returns:
            输入操作结果
        """
        xpath = self.course_search_input()
        log.info(f"输入课程搜索关键词：{search_keyword}，xpath定位为：{xpath}")
        return self.element_input_value(driver, By.XPATH, xpath, search_keyword)

    def click_course_checkbox_by_name(self, driver, course_name):
        """根据课程名称点击复选框

        Args:
            driver: WebDriver实例
            course_name: 课程名称

        Returns:
            点击操作结果
        """
        xpath = self.course_checkbox_by_name(course_name)
        log.info(f"根据课程名称点击复选框，课程名称：{course_name}，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_confirm_add_course_button(self, driver):
        """点击确认添加课程按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.confirm_add_course_button()
        log.info(f"点击确认添加课程按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def update_course_system(self, driver, course_name=None):
        """更新课程体系

        Args:
            driver: WebDriver实例
            course_name: 课程名称

        Returns:
            bool: True表示更新成功，False表示更新失败
        """
        # 切换到iframe
        self.switch_into_training_program_manage_iframe(driver)

        # 点击课程体系标签页
        self.click_tab(driver, "课程体系")
        # 点击添加课程按钮
        self.click_add_course_button(driver)
        # 输入课程搜索关键词
        self.input_course_search(driver, course_name)
        # 点击课程复选框
        self.click_course_checkbox_by_name(driver, course_name)
        # 点击确认添加课程按钮
        self.click_confirm_add_course_button(driver)
        # 断言保存成功提示框是否出现
        result = self.is_save_success_alert_display(driver, content="成功添加")

        # 切出iframe
        self.switch_out_training_program_manage_iframe(driver)

        log.info(f"更新课程体系结果：{result}")
        return result

    # ==================== 课程支撑页面操作方法 ====================

    def click_associate_course_button(self, driver, index=1):
        """点击关联课程按钮

        Args:
            driver: WebDriver实例
            index: 按钮序号，从1开始，默认为1（第1个关联课程按钮）

        Returns:
            点击操作结果
        """
        xpath = self.associate_course_button(index)
        log.info(f"点击关联课程按钮（索引：{index}），xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_course_support_checkbox_by_name(self, driver, course_name):
        """课程支撑页面根据课程名称点击复选框

        Args:
            driver: WebDriver实例
            course_name: 课程名称

        Returns:
            点击操作结果
        """
        xpath = self.course_support_checkbox_by_name(course_name)
        log.info(f"课程支撑页面根据课程名称点击复选框，课程名称：{course_name}，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_course_support_confirm_button(self, driver):
        """点击课程支撑页面关联课程确定按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.course_support_confirm_button()
        log.info(f"点击课程支撑页面关联课程确定按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_course_support_level_option(self, driver, index=1, level="H"):
        """点击课程支撑等级选项

        Args:
            driver: WebDriver实例
            index: 选择按钮序号，从1开始，默认为1（第1个选择按钮）
            level: 支撑等级，H表示高支撑，M表示中支撑，L表示低支撑

        Returns:
            点击操作结果
        """
        xpath = self.course_support_level_option(index, level)
        log.info(f"点击课程支撑等级选项（索引：{index}，支撑等级：{level}），xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def click_complete_edit_button(self, driver):
        """点击完成编辑按钮

        Args:
            driver: WebDriver实例

        Returns:
            点击操作结果
        """
        xpath = self.complete_edit_button()
        log.info(f"点击完成编辑按钮，xpath定位为：{xpath}")
        return self.element_click(driver, By.XPATH, xpath, timeout=10)

    def update_course_support(self, driver, index=1, course_name=None, level="H"):
        """更新课程支撑

        Args:
            driver: WebDriver实例
            index: 关联课程按钮序号，从1开始，默认为1（第1个关联课程按钮）
            course_name: 课程名称
            level: 支撑等级，H表示高支撑，M表示中支撑，L表示低支撑

        Returns:
            bool: True表示更新成功，False表示更新失败
        """
        # 切换到iframe
        self.switch_into_training_program_manage_iframe(driver)
        # 点击课程支撑标签页
        self.click_tab(driver, "课程支撑")
        # 点击关联课程按钮（不传index，每次都选第一个关联课程按钮，因为点击完成编辑后，对应的关联课程按钮会消失）
        self.click_associate_course_button(driver)
        # 点击课程支撑复选框
        self.click_course_support_checkbox_by_name(driver, course_name)
        # 点击课程支撑页面关联课程确定按钮
        self.click_course_support_confirm_button(driver)
        # 点击课程支撑等级选项
        self.click_course_support_level_option(driver, index=index, level=level)
        # 点击完成编辑按钮
        self.click_complete_edit_button(driver)
        # 断言保存成功提示框是否出现
        result = self.is_save_success_alert_display(driver, content="编辑完成")

        # 切出iframe
        self.switch_out_training_program_manage_iframe(driver)

        log.info(f"更新课程支撑结果：{result}")
        return result
