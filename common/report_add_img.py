# encoding: utf-8
# @File  : LoginPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/01/18:31
# @Desc  :
from contextlib import contextmanager
from time import sleep

import allure

from logs.log import log


def add_img_2_report(driver, step_name, need_sleep=True):
    """添加截图到Allure测试报告

    Args:
        driver: WebDriver实例
        step_name: 步骤名称,用于报告中显示
        need_sleep: 是否需要等待1秒,默认True
    """
    if need_sleep:
        sleep(1)  # 等待页面稳定
    allure.attach(driver.get_screenshot_as_png(), step_name + ".png", allure.attachment_type.PNG)  # 截图并添加到报告


def add_img_path_2_report(img_path, step_name):
    """添加图片路径到Allure测试报告

    Args:
        img_path: 图片路径
        step_name: 步骤名称,用于报告中显示
    """
    allure.attach.file(img_path, step_name + ".png", allure.attachment_type.PNG)


@contextmanager
def log_step(step_name):
    """带日志输出的步骤上下文管理器
    
    用于包装 allure.step，在步骤开始和结束时输出日志分隔线
    
    Args:
        step_name: 步骤名称
        
    Usage:
        with allure.step("登录"):
            with log_step("登录"):
                # 执行登录操作
                pass
    """
    log.info("-" * 80)
    log.info(f"【步骤】{step_name}")
    log.info("-" * 80)
    try:
        yield
    finally:
        pass  # 步骤结束时不输出日志，避免冗余
