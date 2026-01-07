# encoding: utf-8
# @File  : driver_config.py
# @Author: 孔敬淳
# @Date  : 2025/12/01/17:52
# @Desc  : Chrome 浏览器驱动配置类

import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from common.tools import get_project_path, sep
from common.yaml_config import GetConf


class DriverConfig:
    # ChromeDriver 镜像配置
    CHROMEDRIVER_URL = "https://mirrors.huaweicloud.com/chromedriver"
    CHROMEDRIVER_LATEST_URL = "https://mirrors.huaweicloud.com/chromedriver/LATEST_RELEASE"

    # 本地ChromeDriver路径（优先使用）
    # Windows系统需要.exe扩展名，Linux/Mac不需要
    _chromedriver_name = "chromedriver.exe" if sys.platform == "win32" else "chromedriver"
    LOCAL_CHROMEDRIVER_PATH = os.path.join(get_project_path(), "driver_files", _chromedriver_name)

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
    def _get_chromedriver_path() -> str:
        """
        获取ChromeDriver路径，根据配置文件决定是否只使用本地路径

        Returns:
            str: ChromeDriver可执行文件路径

        Raises:
            FileNotFoundError: 当本地和网络都无法获取chromedriver时抛出异常
        """
        # 读取配置文件，判断是否本地部署
        try:
            deploy_config = GetConf().get_info("部署环境")
            use_local_only = deploy_config.get("是否本地部署", False) if deploy_config else False
        except Exception:
            # 如果读取配置失败，默认使用本地优先策略
            use_local_only = False

        # 优先使用本地chromedriver
        local_path = DriverConfig.LOCAL_CHROMEDRIVER_PATH

        # 检查文件是否存在（Windows上不检查执行权限，因为Windows不使用Unix权限系统）
        if os.path.exists(local_path):
            # 在Windows上，必须使用.exe扩展名的文件
            if sys.platform == "win32":
                # Windows系统：确保文件有.exe扩展名
                if local_path.endswith('.exe'):
                    return local_path
                # 如果没有.exe扩展名，忽略该文件（可能是其他平台的版本）
            else:
                # 在非Windows系统上检查执行权限
                if os.access(local_path, os.X_OK):
                    return local_path

        # 如果配置为本地部署（只使用本地driver），直接抛出异常
        if use_local_only:
            error_msg = (
                f"无法找到本地ChromeDriver！\n"
                f"配置为本地部署（是否本地部署: true）\n"
                f"本地路径不存在: {local_path}\n"
                f"解决方案：\n"
                f"1. 将匹配的chromedriver文件放置到: {local_path}\n"
                f"2. 确保chromedriver有执行权限: chmod +x {local_path}\n"
                f"3. 确保chromedriver版本与Chrome浏览器版本匹配\n"
                f"4. 如需允许网络下载，请在environment.yaml中设置 是否本地部署: false"
            )
            raise FileNotFoundError(error_msg)

        # 如果本地不存在且允许网络下载，尝试使用webdriver-manager（需要网络）
        try:
            driver_manager = ChromeDriverManager(
                url=DriverConfig.CHROMEDRIVER_URL,
                latest_release_url=DriverConfig.CHROMEDRIVER_LATEST_URL
            )
            return driver_manager.install()
        except Exception as e:
            # 无外网环境下的友好提示
            error_msg = (
                f"无法获取ChromeDriver！\n"
                f"本地路径不存在: {local_path}\n"
                f"网络下载失败（可能是无外网环境）: {str(e)}\n"
                f"解决方案：\n"
                f"1. 将匹配的chromedriver文件放置到: {local_path}\n"
                f"2. 确保chromedriver有执行权限: chmod +x {local_path}\n"
                f"3. 确保chromedriver版本与Chrome浏览器版本匹配"
            )
            raise FileNotFoundError(error_msg) from e

    @staticmethod
    def _create_chrome_service() -> ChromeService:
        """
        创建 ChromeDriver 服务实例

        Returns:
            ChromeService: ChromeDriver 服务对象
        """
        chromedriver_path = DriverConfig._get_chromedriver_path()
        return ChromeService(chromedriver_path)

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
