# encoding: utf-8
# @File  : driver_config.py
# @Author: 孔敬淳
# @Date  : 2025/12/01/17:52
# @Desc  : Chrome 浏览器驱动配置类

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverConfig:
    # ChromeDriver 镜像配置
    CHROMEDRIVER_URL = "https://mirrors.huaweicloud.com/chromedriver"
    CHROMEDRIVER_LATEST_URL = "https://mirrors.huaweicloud.com/chromedriver/LATEST_RELEASE"

    @staticmethod
    def _configure_chrome_options() -> webdriver.ChromeOptions:
        """
        配置 Chrome 浏览器选项

        Returns:
            ChromeOptions: 配置好的 Chrome 选项对象
        """
        options = webdriver.ChromeOptions()

        # 去除"Chrome正受到自动测试软件控制"的提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # 安全与证书相关配置（解决 HTTPS 警告）
        security_args = [
            "--disable-features=HttpsFirstMode",
            "--ignore-certificate-errors",
            "--allow-insecure-localhost",
            "--ignore-ssl-errors=true",
            "--allow-running-insecure-content",
            "--disable-web-security",
            "--disable-site-isolation-trials",
            "--disable-3d-apis",
        ]

        # 系统兼容性配置
        compatibility_args = [
            "--disable-gpu",  # 禁用GPU加速，解决某些系统上的图形渲染问题
            "--no-sandbox",  # 禁用沙箱模式，适用于容器化环境或权限受限的系统
            "--disable-dev-shm-usage",  # 禁用devshm使用，解决内存不足问题
        ]

        # 应用所有配置参数
        for arg in security_args + compatibility_args:
            options.add_argument(arg)

        return options

    @staticmethod
    def _create_chrome_service() -> ChromeService:
        """
        创建 ChromeDriver 服务实例

        Returns:
            ChromeService: ChromeDriver 服务对象
        """
        driver_manager = ChromeDriverManager(
            url=DriverConfig.CHROMEDRIVER_URL,
            latest_release_url=DriverConfig.CHROMEDRIVER_LATEST_URL
        )
        return ChromeService(driver_manager.install())

    @staticmethod
    def driver_config() -> WebDriver:
        """
        初始化 Chrome 浏览器驱动，兼容 Selenium 4.36

        Returns:
            WebDriver: Chrome WebDriver 实例
        """
        options = DriverConfig._configure_chrome_options()
        service = DriverConfig._create_chrome_service()

        # 初始化 Chrome 浏览器实例
        driver = webdriver.Chrome(service=service, options=options)

        # 浏览器窗口设置
        driver.maximize_window()  # 设置浏览器全屏
        driver.delete_all_cookies()  # 删除所有cookies

        return driver
