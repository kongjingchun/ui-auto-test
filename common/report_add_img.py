from time import sleep

import allure


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
