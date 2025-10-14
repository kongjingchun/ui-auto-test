# encoding: utf-8
# @File  : driver_config.py
# @Author: kongjingchun
# @Date  : 2025/10/14/16:14
# @Desc  : 浏览器驱动配置，兼容 Selenium 4.36

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverConfig:
    @staticmethod
    def driver_config():
        """
        初始化 Chrome 浏览器驱动，兼容 Selenium 4.36
        :return: WebDriver 实例
        """
        # 创建 ChromeOptions
        options = webdriver.ChromeOptions()

        # 基础设置
        options.add_argument("--disable-infobars")
        options.add_argument("window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")  # 修正拼写错误：no-sanbox → no-sandbox
        options.add_argument('--disable-dev-shm-usage')

        # 安全与证书相关（解决 HTTPS 警告）
        options.add_argument("--disable-features=HttpsFirstMode")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")
        options.add_argument("--ignore-ssl-errors=true")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-site-isolation-trials")
        options.add_argument("--disable-3d-apis")

        # 无痕模式
        # options.add_argument("--incognito")

        # 去除“Chrome 正受到自动测试软件控制”提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # 设置服务对象
        service = Service(ChromeDriverManager().install())

        # 创建浏览器实例
        driver = webdriver.Chrome(service=service, options=options)

        # 设置隐式等待
        driver.implicitly_wait(3)

        # 清除 cookies
        driver.delete_all_cookies()

        return driver


if __name__ == "__main__":
    DriverConfig().driver_config()
