# encoding: utf-8
# @File  : ObjectMap.py
# @Author: kongjingchun
# @Date  : 2025/12/15/18:22
# @Desc  : 页面元素定位映射类，提供元素定位和等待功能
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ObjectMap:
    @staticmethod
    def wait_for_element(driver: WebDriver, locate_type: By, locator_expression: str,
                         timeout: int = 10, is_visibility: bool = False) -> WebElement:
        """
        等待并获取页面元素对象，支持超时等待和可见性判断

        Args:
            driver: 浏览器驱动对象
            locate_type: 元素定位方式 (By.ID, By.XPATH等)
            locator_expression: 元素定位表达式
            timeout: 超时时间(秒)，默认10秒
            is_visibility: 是否需要元素可见，默认False

        Returns:
            WebElement: 定位到的元素对象

        Raises:
            TimeoutException: 元素定位失败或超时
        """
        try:
            wait = WebDriverWait(driver, timeout)

            if is_visibility:
                # 等待元素可见
                condition = EC.visibility_of_element_located((locate_type, locator_expression))
            else:
                # 只等待元素存在（不一定可见）
                condition = EC.presence_of_element_located((locate_type, locator_expression))

            return wait.until(condition)
        except TimeoutException:
            visibility_text = "可见" if is_visibility else "存在"
            raise TimeoutException(
                f"元素定位失败（等待{visibility_text}），定位方式: {locate_type}，"
                f"定位表达式: {locator_expression}，超时时间: {timeout}秒"
            )

    @staticmethod
    def wait_page_load(driver: WebDriver, timeout: int = 30) -> bool:
        """
        等待页面加载完成
        检查页面 document.readyState 状态，以及 jQuery（如果存在）是否加载完成

        Args:
            driver: 浏览器驱动对象
            timeout: 超时时间(秒)，默认30秒

        Returns:
            bool: 页面加载完成返回True

        Raises:
            TimeoutException: 页面加载超时
        """
        try:
            wait = WebDriverWait(driver, timeout)

            # 等待页面 document.readyState 为 complete
            def page_ready(driver):
                return driver.execute_script("return document.readyState") == "complete"

            # 等待页面加载完成
            wait.until(lambda d: page_ready(d))

            # 如果页面使用了 jQuery，等待 jQuery 加载完成
            try:
                wait.until(lambda d: d.execute_script("return typeof jQuery !== 'undefined' && jQuery.active == 0"))
            except TimeoutException:
                # 如果页面没有使用 jQuery，忽略此错误
                pass

            return True
        except TimeoutException:
            raise TimeoutException(f"页面加载超时，超时时间: {timeout}秒")

    @staticmethod
    def element_disappear(driver: WebDriver, locate_type: By, locator_expression: str,
                          timeout: int = 10) -> bool:
        """
        等待元素消失（不可见或从DOM中移除）
        常用于等待加载动画、提示信息等元素消失

        Args:
            driver: 浏览器驱动对象
            locate_type: 元素定位方式 (By.ID, By.XPATH等)
            locator_expression: 元素定位表达式
            timeout: 超时时间(秒)，默认10秒

        Returns:
            bool: 元素消失返回True

        Raises:
            TimeoutException: 元素未在指定时间内消失
        """
        try:
            wait = WebDriverWait(driver, timeout)
            
            # 等待元素不可见或从DOM中移除
            # invisibility_of_element_located 会处理元素不存在的情况
            condition = EC.invisibility_of_element_located((locate_type, locator_expression))
            
            wait.until(condition)
            return True
        except TimeoutException:
            raise TimeoutException(
                f"元素未消失（超时），定位方式: {locate_type}，"
                f"定位表达式: {locator_expression}，超时时间: {timeout}秒"
            )

    @staticmethod
    def element_appear(driver: WebDriver, locate_type: By, locator_expression: str,
                       timeout: int = 30) -> bool:
        """
        等待元素出现（可见或从DOM中加载）
        常用于等待加载动画、提示信息等元素出现

        Args:
            driver: 浏览器驱动对象
            locate_type: 元素定位方式 (By.ID, By.XPATH等)
            locator_expression: 元素定位表达式
            timeout: 超时时间(秒)，默认30秒

        Returns:
            bool: 元素出现返回True

        Raises:
            TimeoutException: 元素未在指定时间内出现
        """
        try:
            wait = WebDriverWait(driver, timeout)
            condition = EC.presence_of_element_located((locate_type, locator_expression))
            wait.until(condition)
            return True
        except TimeoutException:
            raise TimeoutException(
                f"元素未出现（超时），定位方式: {locate_type}，"
                f"定位表达式: {locator_expression}，超时时间: {timeout}秒"
            )
