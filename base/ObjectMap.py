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

    def wait_for_ready_state_complete(self, driver, timeout=10):
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

    def element_disappear(self, driver, locate_type, locator_expression, timeout=10):
        """
        等待页面元素消失（Selenium 4优化版本）
        :param driver: 浏览器驱动对象
        :param locate_type: 元素定位方式
        :param locator_expression: 元素定位表达式
        :param timeout: 超时时间(秒)
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

    def element_appear(self, driver, locate_type, locator_expression, timeout=10):
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
            # self.element_get(driver, locate_type, locator_expression, timeout, must_be_visible=True)
            res = self.element_get(driver, locate_type, locator_expression, timeout, must_be_visible=True)
            if res:
                return True
            else:
                return False
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

    def element_input_value(self, driver, locate_type, locator_expression, fill_value, timeout=10):
        """
        向元素输入文本
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param fill_value: 输入值
        :param timeout: 超时时间(秒)
        :return: True成功
        """
        # 将输入值转换为字符串
        fill_value = str(fill_value) if isinstance(fill_value, (int, float)) else fill_value

        # 判断是否需要回车
        need_enter = fill_value.endswith("\n")
        if need_enter:
            fill_value = fill_value[:-1]

        log.info(f"向元素 {locator_expression} 输入值 {fill_value}")

        # 获取并操作元素，最多重试2次
        for attempt in range(2):
            try:
                # 等待元素出现并可见
                wait = WebDriverWait(driver, timeout, poll_frequency=0.1)
                element = wait.until(
                    EC.visibility_of_element_located((locate_type, locator_expression))
                )

                # 滚动元素到可视区域中心位置
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
                time.sleep(0.2)  # 等待滚动完成

                # 清除原有值
                try:
                    element.clear()
                except Exception:
                    pass  # 清除失败不影响后续操作

                # 尝试普通输入，如果失败则使用JavaScript输入
                try:
                    # 先尝试点击元素确保获得焦点
                    try:
                        element.click()
                        time.sleep(0.1)
                    except Exception:
                        pass  # 点击失败不影响后续操作

                    # 输入值
                    element.send_keys(fill_value)
                    if need_enter:
                        element.send_keys(Keys.RETURN)

                    # 等待页面就绪
                    self.wait_for_ready_state_complete(driver=driver)
                    return True

                except Exception as send_error:
                    # 普通输入失败，尝试使用JavaScript输入
                    log.info(f"元素 {locator_expression} 普通输入失败，尝试使用JavaScript输入")
                    try:
                        # 如果元素可能过期，重新定位元素
                        try:
                            # 尝试使用现有元素
                            driver.execute_script("arguments[0].value = arguments[1];", element, "")
                        except (StaleElementReferenceException, Exception):
                            # 元素过期，重新定位
                            log.info(f"元素 {locator_expression} 在JavaScript输入时过期，重新定位元素")
                            element = wait.until(
                                EC.presence_of_element_located((locate_type, locator_expression))
                            )
                            driver.execute_script("arguments[0].value = arguments[1];", element, "")

                        # 触发input事件，确保页面响应
                        driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)
                        # 触发change事件
                        driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", element)
                        # 触发click事件
                        try:
                            driver.execute_script("arguments[0].click();", element)
                            time.sleep(0.1)
                            # 使用send_keys输入值
                            element.send_keys(fill_value)
                        except Exception:
                            pass  # click事件触发失败不影响后续操作

                        if need_enter:
                            # 如果元素过期，重新定位后再发送回车
                            try:
                                element.send_keys(Keys.RETURN)
                            except (StaleElementReferenceException, Exception):
                                element = wait.until(
                                    EC.presence_of_element_located((locate_type, locator_expression))
                                )
                                element.send_keys(Keys.RETURN)

                        # 等待页面就绪
                        self.wait_for_ready_state_complete(driver=driver)
                        log.info(f"元素 {locator_expression} 使用JavaScript输入成功")
                        return True
                    except Exception as js_error:
                        # JavaScript输入也失败
                        log.info(f"元素 {locator_expression} JavaScript输入也失败：{str(js_error)}")
                        raise Exception(f"元素 {locator_expression} JavaScript输入也失败：{str(js_error)}")

            except StaleElementReferenceException:
                if attempt == 0:
                    # 第一次失败，等待页面刷新后重试
                    log.warning(f"元素 {locator_expression} 输入时发生stale element异常，等待页面刷新后重试")
                    self.wait_for_ready_state_complete(driver=driver)
                    time.sleep(0.1)
                    continue
                else:
                    # 重试后仍然失败
                    raise Exception(f"元素 {locator_expression} 填值失败：页面元素过期（已重试{attempt + 1}次）")
            except TimeoutException as e:
                # 超时失败
                raise Exception(f"元素 {locator_expression} 填值失败：元素超时未出现或不可交互 - {str(e)}")
            except Exception as e:
                if attempt == 0:
                    log.warning(f"元素 {locator_expression} 输入失败（第{attempt + 1}次尝试），将重试：{str(e)}")
                    time.sleep(0.2)
                    continue
                else:
                    # 重试后仍然失败
                    raise Exception(f"元素 {locator_expression} 填值失败：{str(e)}")

    def element_click(
            self,
            driver,
            locate_type,
            locator_expression,
            locate_type_disappear=None,
            locator_expression_disappear=None,
            locate_type_appear=None,
            locator_expression_appear=None,
            timeout=10
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
        # 最多重试3次，处理stale element和click intercepted异常
        for attempt in range(3):
            try:
                # Selenium 4推荐：使用WebDriverWait等待元素可点击
                wait = WebDriverWait(driver, timeout, poll_frequency=0.1)
                element = wait.until(
                    EC.element_to_be_clickable((locate_type, locator_expression))
                )

                # 滚动元素到可视区域中心位置
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
                time.sleep(0.3)  # 等待滚动完成

                try:
                    element.click()
                except Exception as click_error:
                    # 如果普通点击失败，尝试使用JavaScript点击
                    if "click intercepted" in str(click_error).lower() or "not clickable" in str(click_error).lower():
                        log.warning(f"元素 {locator_expression} 被遮挡或不可点击，尝试使用JavaScript点击")
                        driver.execute_script("arguments[0].click();", element)
                    else:
                        raise

                # 点击后等待元素出现或消失
                if locate_type_appear:
                    self.element_appear(driver, locate_type_appear, locator_expression_appear)
                if locate_type_disappear:
                    self.element_disappear(driver, locate_type_disappear, locator_expression_disappear)

                return True
            except StaleElementReferenceException:
                if attempt < 2:
                    # 前两次失败，等待页面刷新后重试
                    log.warning(f"元素 {locator_expression} 点击时发生stale element异常，等待页面刷新后重试（第{attempt + 1}次）")
                    self.wait_for_ready_state_complete(driver=driver)
                    time.sleep(0.2)
                    continue
                else:
                    log.error(f"元素 {locator_expression} 点击失败：页面元素过期（已重试{attempt + 1}次）")
                    return False
            except (TimeoutException, Exception) as e:
                if attempt < 2:
                    log.warning(f"元素点击失败（第{attempt + 1}次尝试）: {e}")
                    time.sleep(0.3)
                    continue
                log.error(f"元素点击失败（已重试{attempt + 1}次）: {e}")
                return False

    def element_double_click(
            self,
            driver,
            locate_type,
            locator_expression,
            locate_type_disappear=None,
            locator_expression_disappear=None,
            locate_type_appear=None,
            locator_expression_appear=None,
            timeout=10
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
        log.info(f"切换到iframe：{locate_iframe_expression}")
        iframe = self.element_get(driver, locate_iframe_type, locate_iframe_expression)
        driver.switch_to.frame(iframe)
        return True

    def switch_out_iframe(self, driver, to_root=False):
        """
        从iframe切回主文档
        :param driver: 浏览器驱动
        :param to_root: True切回顶层文档，False切回上一层
        :return: None
        """
        # Selenium 4改进：提供更灵活的iframe切换
        log.info("从iframe切回主文档")
        if to_root:
            driver.switch_to.default_content()
        else:
            driver.switch_to.parent_frame()
        return True

    def switch_to_new_window(self, driver):
        """
        切换到最新打开的窗口
        :param driver: 浏览器驱动
        :return: None
        """
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

    def close_current_window(self, driver, switch_to_first=True):
        """
        关闭当前窗口
        :param driver: 浏览器驱动
        :param switch_to_first: 关闭后是否切换到第一个窗口，True切换到第一个窗口，False切换到上一个窗口，默认为True
        :return: True成功，False失败
        """
        try:
            # 获取当前窗口句柄
            current_handle = driver.current_window_handle
            # 获取所有窗口句柄
            all_handles = driver.window_handles

            log.info(f"关闭当前窗口，当前窗口句柄：{current_handle}，总窗口数：{len(all_handles)}")

            # 如果只有一个窗口，不能关闭
            if len(all_handles) <= 1:
                log.warning("只有一个窗口，无法关闭")
                return False

            # 关闭当前窗口
            driver.close()

            # 切换到其他窗口
            remaining_handles = [handle for handle in all_handles if handle != current_handle]
            if remaining_handles:
                if switch_to_first:
                    # 切换到第一个窗口
                    driver.switch_to.window(remaining_handles[0])
                    log.info(f"已切换到第一个窗口，窗口句柄：{remaining_handles[0]}")
                else:
                    # 切换到最后一个窗口（通常是上一个打开的窗口）
                    driver.switch_to.window(remaining_handles[-1])
                    log.info(f"已切换到上一个窗口，窗口句柄：{remaining_handles[-1]}")

            return True
        except Exception as e:
            log.error(f"关闭窗口失败：{str(e)}")
            return False

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

    # 获取元素中值的方法
    def get_element_value(self, driver, locate_type, locator_expression):
        """
        获取表单元素的value属性值（适用于input、textarea等）
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :return: 元素的value属性值
        """
        element = self.element_get(driver, locate_type, locator_expression)
        return element.get_attribute("value")

    def get_element_text(self, driver, locate_type, locator_expression, timeout=10):
        """
        获取元素的文本内容（适用于span、div、p等标签）
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param timeout: 超时时间(秒)
        :return: 元素的文本内容
        """
        element = self.element_get(driver, locate_type, locator_expression, timeout=timeout)
        text = element.text.strip()
        log.info(f"获取元素 {locator_expression} 的文本内容: {text}")
        return text

    def get_element_attribute(self, driver, locate_type, locator_expression, attribute_name, timeout=10):
        """
        获取元素的指定属性值
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param attribute_name: 属性名（如 'class', 'id', 'data-v-0b15bdb0' 等）
        :param timeout: 超时时间(秒)
        :return: 属性值
        """
        element = self.element_get(driver, locate_type, locator_expression, timeout=timeout)
        attr_value = element.get_attribute(attribute_name)
        log.info(f"获取元素 {locator_expression} 的属性 {attribute_name}: {attr_value}")
        return attr_value

    def page_contains_text(self, driver, text, case_sensitive=False):
        """
        判断当前页面是否包含指定文字
        :param driver: 浏览器驱动
        :param text: 要查找的文字
        :param case_sensitive: 是否区分大小写，True区分大小写，False不区分（默认）
        :return: True表示页面包含该文字，False表示不包含
        """
        try:
            # 获取页面源码
            page_source = driver.page_source

            if case_sensitive:
                # 区分大小写
                contains = text in page_source
            else:
                # 不区分大小写
                contains = text.lower() in page_source.lower()

            log.info(f"检查页面是否包含文字'{text}'（区分大小写：{case_sensitive}）：{contains}")
            return contains
        except Exception as e:
            log.error(f"判断页面是否包含文字失败：{str(e)}")
            return False

    def diagnose_input_element(self, driver, locate_type, locator_expression, timeout=10):
        """
        诊断输入框元素状态，帮助排查输入失败的原因
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param timeout: 超时时间(秒)
        :return: 诊断信息字典
        """
        diagnosis = {
            "element_found": False,
            "element_visible": False,
            "element_enabled": False,
            "is_readonly": False,
            "is_disabled": False,
            "tag_name": None,
            "error": None
        }

        try:
            # 尝试定位元素
            element = self.element_get(driver, locate_type, locator_expression, timeout)
            diagnosis["element_found"] = True
            diagnosis["tag_name"] = element.tag_name

            # 检查元素是否可见
            try:
                is_displayed = element.is_displayed()
                diagnosis["element_visible"] = is_displayed
            except Exception as e:
                diagnosis["error"] = f"检查可见性失败：{str(e)}"

            # 检查元素是否启用
            try:
                is_enabled = element.is_enabled()
                diagnosis["element_enabled"] = is_enabled
            except Exception as e:
                diagnosis["error"] = f"检查启用状态失败：{str(e)}"

            # 检查readonly属性
            try:
                readonly = element.get_attribute("readonly")
                diagnosis["is_readonly"] = readonly is not None and readonly != "false"
            except Exception as e:
                pass

            # 检查disabled属性
            try:
                disabled = element.get_attribute("disabled")
                diagnosis["is_disabled"] = disabled is not None and disabled != "false"
            except Exception as e:
                pass

            log.info(f"元素诊断结果：{diagnosis}")
            return diagnosis

        except Exception as e:
            diagnosis["error"] = f"元素定位失败：{str(e)}"
            log.error(f"元素诊断失败：{str(e)}")
            return diagnosis
