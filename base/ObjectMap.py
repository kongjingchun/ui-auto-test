import datetime
import os.path
import time
from urllib.parse import urljoin

from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

from common.yaml_config import GetConf
from common.tools import get_project_path, sep


class ObjectMap:
    # 获取基础地址
    url = GetConf().get_url()

    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_be_visible=False):
        """
        单个元素获取
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :param must_be_visible: 元素是否必须可见，True是必须可见，False是默认值
        :return: 返回的元素
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 设置的结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            # 查找元素
            try:
                element = driver.find_element(by=locate_type, value=locator_expression)
                # 如果元素不是必须可见的，就直接返回元素
                if not must_be_visible:
                    return element
                # 如果元素必须是可见的，则需要先判断元素是否可见
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break
                pass
            time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败，定位方式：" + locate_type + " 定位表达式：" + locator_expression)

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """
        等待页面完全加载完成
        通过检查 document.readyState 状态来判断页面是否加载完成
        
        Args:
            driver: 浏览器驱动对象
            timeout: 超时时间(秒)，默认30秒
            
        Returns:
            bool: 页面加载完成返回True
            
        Raises:
            TimeoutError: 页面在超时时间内未完全加载完成
            WebDriverException: WebDriver执行JavaScript失败
        """
        # 计算结束时间（使用秒为单位，更简洁）
        end_time = time.time() + timeout
        # 轮询间隔（秒）
        poll_interval = 0.1

        # 持续检查页面状态直到超时或加载完成
        while time.time() < end_time:
            try:
                # 获取页面的 readyState 状态
                # readyState 可能的值：
                # - "loading": 文档仍在加载
                # - "interactive": 文档已完成加载，但子资源仍在加载
                # - "complete": 文档和所有子资源已完成加载
                ready_state = driver.execute_script("return document.readyState")

                # 如果页面完全加载完成，等待一小段时间确保页面稳定，然后返回
                if ready_state == "complete":
                    time.sleep(0.01)  # 短暂等待，确保页面完全稳定
                    return True

            except WebDriverException as e:
                # WebDriver执行JavaScript失败，可能是页面还未完全初始化
                # 如果接近超时时间，抛出异常；否则继续等待
                if time.time() >= end_time - poll_interval:
                    raise WebDriverException(
                        f"等待页面加载时WebDriver执行JavaScript失败，超时时间: {timeout}秒，错误: {str(e)}"
                    )
                # 继续等待，给页面一些时间初始化
                pass

            # 等待一段时间后再次检查
            time.sleep(poll_interval)

        # 超时后仍未加载完成，抛出异常
        raise TimeoutError(
            f"页面在{timeout}秒后仍然没有完全加载完成（readyState未达到'complete'）"
        )

    def element_disappear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素消失
        :param driver:浏览器驱动
        :param locate_type:定位方式类型
        :param locator_expression:定位表达式
        :param timeout:超时时间
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 设置的结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception("元素没有消失，定位方式:" + locate_type + "\n定位表达式:" + locator_expression)
        else:
            pass

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素出现并返回元素对象
        持续检查元素是否存在且可见，直到超时或元素出现
        
        Args:
            driver: 浏览器驱动对象
            locate_type: 元素定位方式（如 By.ID, By.XPATH等），为None则直接返回None
            locator_expression: 元素定位表达式
            timeout: 超时时间(秒)，默认30秒
            
        Returns:
            WebElement: 找到的元素对象
            
        Raises:
            ElementNotVisibleException: 元素在超时时间内未出现或不可见
        """
        # 如果定位方式为None，直接返回None（不进行等待）
        if not locate_type:
            return None

        # 计算结束时间（使用秒为单位，更简洁）
        end_time = time.time() + timeout
        # 轮询间隔（秒）
        poll_interval = 0.1

        # 持续轮询直到超时或元素出现
        while time.time() < end_time:
            try:
                # 查找元素
                element = driver.find_element(by=locate_type, value=locator_expression)

                # 检查元素是否可见
                if element.is_displayed():
                    return element
                # 如果元素存在但不可见，继续等待

            except NoSuchElementException:
                # 元素不存在，继续等待
                pass
            except StaleElementReferenceException:
                # 元素引用已失效，继续等待（元素可能正在重新渲染）
                pass
            except Exception as e:
                # 其他异常（如WebDriverException等），继续等待
                # 这些异常可能是暂时的，给元素一些时间出现
                pass

            # 等待一段时间后再次检查
            time.sleep(poll_interval)

        # 超时后仍未找到元素，抛出异常
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
            locator_expression_appear=None,
            timeout=30
    ):
        """
        导航到指定URL并等待页面元素状态变化
        先等待页面加载完成，然后等待指定元素消失（如果提供），最后等待指定元素出现（如果提供）
        
        Args:
            driver: 浏览器驱动对象
            url: 要访问的URL（相对路径或绝对路径）
            locate_type_disappear: 等待页面元素消失的定位方式，为None则跳过
            locator_expression_disappear: 等待页面元素消失的定位表达式
            locate_type_appear: 等待页面元素出现的定位方式，为None则跳过
            locator_expression_appear: 等待页面元素出现的定位表达式
            timeout: 超时时间(秒)，默认30秒
            
        Returns:
            bool: 操作成功返回True，失败返回False
        """

        # 初始化full_url变量，用于异常处理
        full_url = str(url)

        try:
            # 构建完整URL
            # 如果URL是绝对路径（以http://或https://开头），直接使用
            if str(url).startswith(("http://", "https://")):
                full_url = url
            else:
                # 使用urljoin处理相对路径，更安全可靠
                # 确保base_url以/结尾，以便urljoin正确工作
                base_url = self.url
                if not base_url.endswith("/"):
                    base_url += "/"
                # 去掉url开头的/，避免重复
                url_path = str(url).lstrip("/")
                full_url = urljoin(base_url, url_path)

            # 导航到URL
            driver.get(full_url)

            # 等待页面元素都加载完成
            self.wait_for_ready_state_complete(driver, timeout=timeout)

            # 如果提供了消失元素的定位信息，等待元素消失
            # element_disappear方法内部会检查locate_type是否为None
            if locate_type_disappear is not None:
                self.element_disappear(
                    driver,
                    locate_type_disappear,
                    locator_expression_disappear,
                    timeout=timeout
                )

            # 如果提供了出现元素的定位信息，等待元素出现
            # element_appear方法内部会检查locate_type是否为None
            if locate_type_appear is not None:
                self.element_appear(
                    driver,
                    locate_type_appear,
                    locator_expression_appear,
                    timeout=timeout
                )

            return True

        except WebDriverException as e:
            # WebDriver相关异常（如网络错误、页面加载失败等）
            print(f"跳转地址失败：WebDriver异常，URL: {full_url}，错误: {str(e)}")
            return False
        except ElementNotVisibleException as e:
            # 元素可见性异常
            print(f"跳转地址失败：元素等待超时，URL: {full_url}，错误: {str(e)}")
            return False
        except Exception as e:
            # 其他未知异常
            print(f"跳转地址失败：发生未知错误，URL: {full_url}，错误: {str(e)}")
            return False

    def element_is_display(self, driver, locate_type, locator_expression):
        """
        元素是否显示
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        try:
            driver.find_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False

    def element_fill_value(self, driver, locate_type, locator_expression, fill_value, timeout=30):
        """
        向页面元素填充值（输入文本）
        支持自动处理换行符（\n），如果值以换行符结尾，会在输入后自动按回车键
        
        Args:
            driver: 浏览器驱动对象
            locate_type: 元素定位方式
            locator_expression: 元素定位表达式
            fill_value: 要填充的值（支持字符串、数字等类型）
            timeout: 等待元素出现的超时时间(秒)，默认30秒
            
        Returns:
            bool: 填充成功返回True，失败抛出异常
        """
        # 将填充值转换为字符串
        fill_value = str(fill_value)

        # 提取输入值和是否需要按回车
        need_enter = fill_value.endswith("\n")
        input_value = fill_value[:-1] if need_enter else fill_value

        # 重试机制：最多重试2次（处理StaleElementReferenceException）
        max_retries = 2
        for attempt in range(max_retries):
            try:
                # 等待元素出现并获取元素对象
                element = self.element_appear(
                    driver,
                    locate_type=locate_type,
                    locator_expression=locator_expression,
                    timeout=timeout
                )

                # 清空元素原有内容
                element.clear()

                # 输入值
                element.send_keys(input_value)

                # 如果需要按回车，发送回车键
                if need_enter:
                    element.send_keys(Keys.RETURN)

                # 等待页面状态稳定
                self.wait_for_ready_state_complete(driver=driver)

                return True

            except StaleElementReferenceException:
                # 元素引用已失效，等待页面刷新后重试
                if attempt < max_retries - 1:
                    self.wait_for_ready_state_complete(driver=driver)
                    time.sleep(0.06)
                    continue
                else:
                    # 最后一次重试也失败，抛出异常
                    raise Exception(f"元素填值失败：元素引用已过时，定位方式: {locate_type}，定位表达式: {locator_expression}")

            except Exception as e:
                # 其他异常直接抛出，提供更详细的错误信息
                raise Exception(f"元素填值失败：定位方式: {locate_type}，定位表达式: {locator_expression}，错误: {str(e)}")

        # 如果所有重试都失败（理论上不会执行到这里，因为会抛出异常）
        raise Exception(f"元素填值失败：重试{max_retries}次后仍然失败，定位方式: {locate_type}，定位表达式: {locator_expression}")

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
        点击页面元素并等待相关元素状态变化
        先等待元素出现，然后点击元素，最后等待指定元素出现或消失（如果提供）
        
        Args:
            driver: 浏览器驱动对象
            locate_type: 要点击的元素定位方式
            locator_expression: 要点击的元素定位表达式
            locate_type_disappear: 点击后等待消失的元素定位方式，为None则跳过
            locator_expression_disappear: 点击后等待消失的元素定位表达式
            locate_type_appear: 点击后等待出现的元素定位方式，为None则跳过
            locator_expression_appear: 点击后等待出现的元素定位表达式
            timeout: 超时时间(秒)，默认30秒
            
        Returns:
            bool: 操作成功返回True，失败返回False
        """
        # 参数验证：检查必需的定位参数
        if not locate_type or not locator_expression:
            print("错误: locate_type 和 locator_expression 不能为空")
            return False

        # 重试机制：最多重试2次（处理StaleElementReferenceException）
        max_retries = 2
        for attempt in range(max_retries):
            try:
                # 等待元素出现并获取元素对象
                element = self.element_appear(
                    driver=driver,
                    locate_type=locate_type,
                    locator_expression=locator_expression,
                    timeout=timeout
                )

                # 如果元素为None（定位方式为None时返回None），直接返回
                if element is None:
                    print("警告: 元素定位方式为None，跳过点击操作")
                    return False

                # 点击元素
                element.click()

                # 点击成功，跳出重试循环
                break

            except StaleElementReferenceException:
                # 元素引用已失效，等待页面刷新后重试
                if attempt < max_retries - 1:
                    self.wait_for_ready_state_complete(driver=driver)
                    time.sleep(0.06)  # 短暂等待，确保页面刷新
                    continue
                else:
                    # 最后一次重试也失败
                    print(f"元素点击失败：元素引用已过时，定位方式: {locate_type}，"
                          f"定位表达式: {locator_expression}")
                    return False

            except ElementNotVisibleException as e:
                # 元素未出现或不可见
                print(f"元素点击失败：元素未出现或不可见，定位方式: {locate_type}，"
                      f"定位表达式: {locator_expression}，错误: {str(e)}")
                return False

            except Exception as e:
                # 其他异常（如元素不可点击、被遮挡等）
                print(f"元素点击失败：发生未知错误，定位方式: {locate_type}，"
                      f"定位表达式: {locator_expression}，错误: {str(e)}")
                return False

        # 点击成功后，等待相关元素状态变化（如果提供了定位参数）
        try:
            # 如果提供了出现元素的定位信息，等待元素出现
            # element_appear方法内部会检查locate_type是否为None
            if locate_type_appear is not None:
                self.element_appear(
                    driver,
                    locate_type_appear,
                    locator_expression_appear,
                    timeout=timeout
                )

            # 如果提供了消失元素的定位信息，等待元素消失
            # element_disappear方法内部会检查locate_type是否为None
            if locate_type_disappear is not None:
                self.element_disappear(
                    driver,
                    locate_type_disappear,
                    locator_expression_disappear,
                    timeout=timeout
                )

        except ElementNotVisibleException as e:
            # 元素等待超时
            print(f"等待元素状态变化失败：元素等待超时，错误: {str(e)}")
            return False
        except Exception as e:
            # 其他异常
            print(f"等待元素状态变化失败：发生未知错误，错误: {str(e)}")
            return False

        return True

    def upload(self, driver, locate_type, locator_expression, file_path):
        """
        文件上传功能

        Args:
            driver: 浏览器驱动对象
            locate_type: 文件上传元素的定位方式
            locator_expression: 文件上传元素的定位表达式
            file_path: 要上传的文件路径

        Returns:
            WebElement.send_keys()方法的返回值

        Raises:
            ElementNotVisibleException: 元素定位失败或元素不可见
        """
        # 获取文件上传输入框元素
        element = self.element_get(driver, locate_type, locator_expression)
        # 通过send_keys方法上传文件
        return element.send_keys(file_path)

