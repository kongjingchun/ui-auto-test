import datetime
import os.path
import time

from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.yaml_config import GetConf
from common.tools import get_project_path, sep
from common.find_img import FindImg
from common.report_add_img import add_img_path_2_report
from logs.log import log


class ObjectMap:
    """Web元素操作基础类，提供元素定位、等待、交互等核心功能"""
    # 获取基础URL
    url = GetConf().get_url()

    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_be_visible=False):
        """
        单个元素获取（Selenium 4优化版本）
        :param driver: 浏览器驱动对象
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间(秒)，默认10秒
        :param must_be_visible: 元素是否必须可见，True是必须可见，False是默认值
        :return: 返回的元素
        """
        try:
            # Selenium 4推荐：使用WebDriverWait + expected_conditions
            wait = WebDriverWait(driver, timeout, poll_frequency=0.1)

            if must_be_visible:
                # 元素必须可见
                element = wait.until(
                    EC.visibility_of_element_located((locate_type, locator_expression))
                )
            else:
                # 元素存在即可，不需要可见
                element = wait.until(
                    EC.presence_of_element_located((locate_type, locator_expression))
                )

            log.info(f"元素 {locator_expression} 已通过 {locate_type} 方式找到")
            return element

        except TimeoutException:
            raise ElementNotVisibleException(
                f"元素定位失败（超时{timeout}秒），定位方式: {locate_type}，"
                f"定位表达式: {locator_expression}"
            )

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """
        等待页面完全加载
        :param driver: 浏览器驱动
        :param timeout: 超时时间(秒)，默认30秒
        :return: True表示加载完成
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 设置的结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                # 获取页面的状态
                ready_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                # 如果有driver的错误，执行js会失败，就直接跳过
                time.sleep(0.03)
                return True
            # 如果页面元素全部加载完成，返回True
            if ready_state == "complete":
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                # 如果超时了就break
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        raise Exception("打开网页时，页面元素在%s秒后仍然没有完全加载完" % timeout)

    def element_disappear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素消失（Selenium 4优化版本）
        :param driver: 浏览器驱动对象
        :param locate_type: 元素定位方式
        :param locator_expression: 元素定位表达式
        :param timeout: 超时时间(秒)，默认30秒
        :return: 元素消失返回True
        """
        if not locate_type:
            return True

        try:
            # Selenium 4推荐：使用WebDriverWait + expected_conditions
            wait = WebDriverWait(driver, timeout, poll_frequency=0.1)
            wait.until(
                EC.invisibility_of_element_located((locate_type, locator_expression))
            )
            return True
        except TimeoutException:
            raise Exception(
                f"元素没有消失（超时{timeout}秒），定位方式: {locate_type}，"
                f"定位表达式: {locator_expression}"
            )

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素出现并返回元素对象（Selenium 4优化版本）
        :param driver: 浏览器驱动对象
        :param locate_type: 元素定位方式，为None则直接返回None
        :param locator_expression: 元素定位表达式
        :param timeout: 超时时间(秒)，默认30秒
        :return: 找到的元素对象
        """
        if not locate_type:
            return None

        try:
            # Selenium 4推荐：使用WebDriverWait + expected_conditions
            element = self.element_get(driver, locate_type, locator_expression, timeout)
            return element
        except TimeoutException:
            raise ElementNotVisibleException(
                f"元素没有出现（超时{timeout}秒），定位方式: {locate_type}，"
                f"定位表达式: {locator_expression}"
            )

    def element_to_url(
            self,
            driver,
            url,
            locate_type_disappear=None,
            locator_expression_disappear=None,
            locate_type_appear=None,
            locator_expression_appear=None
    ):
        """
        跳转到指定URL并等待元素状态变化
        :param driver: 浏览器驱动
        :param url: 目标URL
        :param locate_type_disappear: 等待消失的元素定位方式
        :param locator_expression_disappear: 等待消失的元素定位表达式
        :param locate_type_appear: 等待出现的元素定位方式
        :param locator_expression_appear: 等待出现的元素定位表达式
        :return: True成功，False失败
        """
        try:
            driver.get(self.url + url)
            # 等待页面元素都加载完成
            self.wait_for_ready_state_complete(driver)
            # 跳转地址后等待元素消失
            self.element_disappear(
                driver,
                locate_type_disappear,
                locator_expression_disappear
            )
            # 跳转地址后等待元素出现
            self.element_appear(
                driver,
                locate_type_appear,
                locator_expression_appear
            )
        except Exception as e:
            print("跳转地址出现异常，异常原因:%s" % e)
            return False
        return True

    def element_is_display(self, driver, locate_type, locator_expression, timeout=5):
        """
        检查元素是否显示（Selenium 4优化版本）
        :param driver: 浏览器驱动对象
        :param locate_type: 元素定位方式
        :param locator_expression: 元素定位表达式
        :param timeout: 超时时间(秒)，默认5秒
        :return: 元素存在且可见返回True，否则返回False
        """
        try:
            # Selenium 4推荐：使用WebDriverWait检查元素可见性
            self.element_get(driver, locate_type, locator_expression, timeout, must_be_visible=True)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def action_move_to_element(self, driver, locate_type, locator_expression, timeout=10):
        """
        鼠标悬停到指定元素
        :param driver: 浏览器驱动对象
        :param locate_type: 元素定位方式
        :param locator_expression: 元素定位表达式
        :param timeout: 等待元素出现的超时时间(秒)，默认10秒
        :param auto_search_iframes: 是否自动在iframe中查找元素，默认True
        :return: True 表示悬停操作成功执行
        """
        # 获取目标元素
        element = self.element_get(driver, locate_type, locator_expression, timeout=timeout)
        # 创建 ActionChains 对象并执行鼠标悬停
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        return True

    def element_input_value(self, driver, locate_type, locator_expression, fill_value, timeout=30):
        """
        向元素输入文本
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param fill_value: 输入值
        :param timeout: 超时时间(秒)，默认30秒
        :return: True成功
        """
        # 元素必须先出现
        element = self.element_appear(
            driver,
            locate_type=locate_type,
            locator_expression=locator_expression,
            timeout=timeout
        )
        try:
            # 先清除元素中的原有值
            element.clear()
        except StaleElementReferenceException:  # 页面元素没有刷新出来，就对元素进行捕获，从而引发了这个异常
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(
                driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout
            )
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass
        # 填入的值转成字符串
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)
        try:
            # 填入的值不是以\n结尾
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type=locate_type, locator_expression=locator_expression)
            element.clear()
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except Exception:
            raise Exception("元素填值失败")

        return True

    def element_double_click(
            self,
            driver,
            locate_type,
            locator_expression,
            locate_type_disappear=None,
            locator_expression_disappear=None,
            locate_type_appear=None,
            locator_expression_appear=None,
            timeout=30
    ):
        """
        双击元素
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param locate_type_disappear: 等待消失的元素定位方式
        :param locator_expression_disappear: 等待消失的元素定位表达式
        :param locate_type_appear: 等待出现的元素定位方式
        :param locator_expression_appear: 等待出现的元素定位表达式
        :param timeout: 超时时间(秒)，默认30秒
        :return: True成功，False失败
        """
        try:
            # Selenium 4推荐：使用WebDriverWait等待元素可点击
            wait = WebDriverWait(driver, timeout, poll_frequency=0.1)
            element = wait.until(
                EC.element_to_be_clickable((locate_type, locator_expression))
            )
            element.click()

            # 点击后等待元素出现或消失
            if locate_type_appear:
                self.element_appear(driver, locate_type_appear, locator_expression_appear)
            if locate_type_disappear:
                self.element_disappear(driver, locate_type_disappear, locator_expression_disappear)

            return True
        except (TimeoutException, Exception) as e:
            log.error(f"元素点击失败: {e}")
            return False

    def element_click(
            self,
            driver,
            locate_type,
            locator_expression,
            locate_type_disappear=None,
            locator_expression_disappear=None,
            locate_type_appear=None,
            locator_expression_appear=None,
            timeout=30
    ):
        """
        点击元素
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param locate_type_disappear: 等待消失的元素定位方式
        :param locator_expression_disappear: 等待消失的元素定位表达式
        :param locate_type_appear: 等待出现的元素定位方式
        :param locator_expression_appear: 等待出现的元素定位表达式
        :param timeout: 超时时间(秒)，默认30秒
        :return: True成功，False失败
        """
        try:
            # Selenium 4推荐：使用WebDriverWait等待元素可点击
            wait = WebDriverWait(driver, timeout, poll_frequency=0.1)
            element = wait.until(
                EC.element_to_be_clickable((locate_type, locator_expression))
            )
            element.click()

            # 点击后等待元素出现或消失
            if locate_type_appear:
                self.element_appear(driver, locate_type_appear, locator_expression_appear)
            if locate_type_disappear:
                self.element_disappear(driver, locate_type_disappear, locator_expression_disappear)

            return True
        except (TimeoutException, Exception) as e:
            log.error(f"元素点击失败: {e}")
            return False

    def upload(self, driver, locate_type, locator_expression, file_path):
        """
        上传文件
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param file_path: 文件路径
        :return: 上传结果
        """
        element = self.element_get(driver, locate_type, locator_expression)
        return element.send_keys(file_path)

    def switch_into_iframe(self, driver, locate_iframe_type, locate_iframe_expression):
        """
        切换到iframe
        :param driver: 浏览器驱动
        :param locate_iframe_type: iframe定位方式
        :param locate_iframe_expression: iframe定位表达式
        :return: None
        """
        iframe = self.element_get(driver, locate_iframe_type, locate_iframe_expression)
        driver.switch_to.frame(iframe)

    def switch_from_iframe_to_content(self, driver, to_root=False):
        """
        从iframe切回主文档
        :param driver: 浏览器驱动
        :param to_root: True切回顶层文档，False切回上一层
        :return: None
        """
        # Selenium 4改进：提供更灵活的iframe切换
        if to_root:
            driver.switch_to.default_content()
        else:
            driver.switch_to.parent_frame()

    def switch_window_2_latest_handle(self, driver):
        """
        切换到最新打开的窗口
        :param driver: 浏览器驱动
        :return: None
        """
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

    def find_img_in_source(self, driver, img_name):
        """
        在页面截图中查找指定图片
        :param driver: 浏览器驱动
        :param img_name: 图片文件名
        :return: 匹配置信度
        """
        # 截图后图片保存的路径
        source_img_path = get_project_path() + sep(["img", "source_img", img_name], add_sep_before=True)
        print("source_img_path:", source_img_path)
        # 需要查找的图片的路径
        search_img_path = get_project_path() + sep(["img", "assert_img", img_name], add_sep_before=True)
        print("search_img_path:", search_img_path)
        # 截图并保存图片
        driver.get_screenshot_as_file(source_img_path)
        time.sleep(3)
        add_img_path_2_report(source_img_path, "原图")
        add_img_path_2_report(search_img_path, "需要查找的图")
        # 在原图中查找是否有指定的图片，返回信心值
        confidence = FindImg().get_confidence(source_img_path, search_img_path)
        return confidence

    def element_screenshot(self, driver, locate_type, locator_expression):
        """
        对指定元素截图
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :return: 截图文件路径
        """
        ele_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        ele_img_dir_path = get_project_path() + sep(["img", "ele_img"], add_sep_before=True, add_sep_after=True)
        if not os.path.exists(ele_img_dir_path):
            os.mkdir(ele_img_dir_path)
        ele_img_path = ele_img_dir_path + ele_name
        self.element_get(driver, locate_type, locator_expression).screenshot(ele_img_path)
        return ele_img_path

    def scroll_to_element(self, driver, locate_type, locator_expression):
        """
        滚动页面至元素可见
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :return: True成功
        """
        ele = self.element_get(driver, locate_type, locator_expression)
        driver.execute_script("arguments[0].scrollIntoView()", ele)
        return True
