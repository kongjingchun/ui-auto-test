# encoding: utf-8
# @File  : TrainingProgramRevisionPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 培养方案修订页面对象类，封装培养方案修订相关的页面操作方法

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.ai_major.TrainingProgramRevisionBase import TrainingProgramRevisionBase
from logs.log import log


class TrainingProgramRevisionPage(TrainingProgramRevisionBase, ObjectMap):
    """培养方案修订页面类

    继承TrainingProgramRevisionBase和ObjectMap类，提供培养方案修订页面的元素操作方法
    包含6个子页面：专业信息、培养目标、毕业要求、课程设置、实践教学、课程支撑
    """

    # ==================== 通用操作方法 ====================
    def click_tab(self, driver, tab_name):
        """点击标签页

        Args:
            driver: WebDriver实例
            tab_name: 标签页名称，如 '专业信息'、'培养目标'、'毕业要求'、'课程设置'、'实践教学'、'课程支撑'

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

    def is_save_success_alert_display(self, driver):
        """查看保存成功提示框是否出现

        Args:
            driver: WebDriver实例

        Returns:
            bool: True表示保存成功提示框出现，False表示未出现
        """
        xpath = self.save_success_alert()
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

        Returns:
            更新操作结果
        """
        # 点击专业信息标签页
        self.click_tab(driver, "专业信息")
        # 输入专业描述
        self.input_major_description(driver, description)
        # 点击保存按钮
        self.click_save_button(driver)
        # 断言保存成功提示框是否出现
        result = self.is_save_success_alert_display(driver)
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
        """
        # 点击培养目标标签页
        self.click_tab(driver, "培养目标")
        # 输入培养目标概述
        self.input_training_objective_overview(driver, overview)
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

    # 更新毕业要求
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
        """
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
        self.click_add_decomposed_indicator_point_button(driver, decomposed_indicator_index)
        # 输入分解指标点名称
        self.input_decomposed_indicator_point_name(driver, decomposed_indicator_name, indicator_index, decomposed_indicator_index)
        # 输入分解指标点描述
        self.input_decomposed_indicator_point_description(driver, decomposed_indicator_description, indicator_index, decomposed_indicator_index)
        # 点击保存按钮
        self.click_save_button(driver)
        # 断言保存成功提示框是否出现
        result = self.is_save_success_alert_display(driver)
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
        """
        # 点击目标支撑选择按钮
        self.click_target_support_select_button(driver, index)
        # 点击目标支撑等级选项
        self.click_target_support_level_option(driver, level)
        # 点击保存按钮
        self.click_save_button(driver)
        # 断言保存成功提示框是否出现
        result = self.is_save_success_alert_display(driver)
        log.info(f"更新目标支撑结果：{result}")
        return result
    # ==================== 课程设置页面操作方法 ====================

    # ==================== 实践教学页面操作方法 ====================

    # ==================== 课程支撑页面操作方法 ====================
