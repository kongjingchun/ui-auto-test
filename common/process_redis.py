# encoding: utf-8
# @File  : process_redis.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/18:06
# @Desc  : 测试进度管理类，通过Redis记录测试执行进度

import redis
from logs.log import log

from common.tools import get_now_time
from common.redis_operation import RedisOperation


class Process:
    """测试进度管理类，使用Redis存储测试执行进度和结果"""

    def __init__(self):
        """初始化Redis客户端和键名"""
        try:
            self.redis_client = RedisOperation().redis_client
            # 测试Redis连接
            self.redis_client.ping()
        except (redis.ConnectionError, redis.TimeoutError, AttributeError) as e:
            log.error(f"Redis连接失败: {e}")
            raise Exception(f"无法连接到Redis服务器，请检查Redis配置和连接状态: {e}")
        except Exception as e:
            log.error(f"初始化Redis客户端失败: {e}")
            raise

        self.UI_AUTOTEST_PROCESS = "ui_autotest_process"      # 进度信息键
        self.FAILED_TESTCASES_NAMES = "failed_testcase_name"  # 失败用例键
        self.SUCCESS_TESTCASES_NAMES = "success_testcase_name"  # 成功用例键
        self.RUNNING_STATUS = "running_status"                # 运行状态键

    def reset_all(self):
        """清空所有进度数据"""
        try:
            self.redis_client.delete(self.UI_AUTOTEST_PROCESS)
            self.redis_client.delete(self.FAILED_TESTCASES_NAMES)
            self.redis_client.delete(self.SUCCESS_TESTCASES_NAMES)
            self.redis_client.delete(self.RUNNING_STATUS)
        except Exception as e:
            log.error(f"清空进度数据失败: {e}")
            raise

    def init_process(self, total):
        """初始化测试进度

        Args:
            total: 测试用例总数
        """
        try:
            self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "total", str(total))
            self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "success", "0")
            self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "fail", "0")
            self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "start_time", str(get_now_time()))
            self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "end_time", "")
            self.redis_client.set(self.RUNNING_STATUS, "1")
        except Exception as e:
            log.error(f"初始化测试进度失败: {e}")
            raise

    def update_success(self):
        """成功用例数+1"""
        try:
            self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "success", 1)
        except Exception as e:
            log.error(f"更新成功用例数失败: {e}")
            raise

    def update_fail(self):
        """失败用例数+1"""
        try:
            self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "fail", 1)
        except Exception as e:
            log.error(f"更新失败用例数失败: {e}")
            raise

    def insert_into_fail_testcase_names(self, fail_testcase_name):
        """记录失败用例名称

        Args:
            fail_testcase_name: 失败的测试用例名称
        """
        try:
            self.redis_client.lpush(self.FAILED_TESTCASES_NAMES, fail_testcase_name)
        except Exception as e:
            log.error(f"记录失败用例名称失败: {e}")
            raise

    def insert_into_success_testcase_names(self, success_testcase_name):
        """记录成功用例名称

        Args:
            success_testcase_name: 成功的测试用例名称
        """
        try:
            self.redis_client.lpush(self.SUCCESS_TESTCASES_NAMES, success_testcase_name)
        except Exception as e:
            log.error(f"记录成功用例名称失败: {e}")
            raise

    def get_result(self):
        """获取测试结果统计

        Returns:
            tuple: (总数, 成功数, 失败数, 开始时间)
        """
        try:
            total_str = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "total")
            total = int(total_str) if total_str is not None and total_str != '' else 0  # type: ignore

            success_str = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "success")
            success = int(success_str) if success_str is not None and success_str != '' else 0  # type: ignore

            fail_str = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "fail")
            fail = int(fail_str) if fail_str is not None and fail_str != '' else 0  # type: ignore

            start_time = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "start_time")
            start_time = start_time if start_time is not None else '-'

            return total, success, fail, start_time
        except (ValueError, TypeError) as e:
            log.error(f"获取测试结果统计失败，数据类型转换错误: {e}")
            return 0, 0, 0, '-'
        except Exception as e:
            log.error(f"获取测试结果统计失败: {e}")
            return 0, 0, 0, '-'

    def get_process(self):
        """计算测试进度百分比

        Returns:
            str: 进度百分比，如"50.0%"
        """
        try:
            total, success, fail, _ = self.get_result()
            if total == 0:
                return "0%"
            else:
                percentage = (success + fail) / total * 100
                return "%.1f%%" % percentage
        except Exception as e:
            log.error(f"计算测试进度百分比失败: {e}")
            return "0%"

    def get_fail_testcase_names(self):
        """获取所有失败用例名称列表

        Returns:
            list: 失败用例名称列表
        """
        try:
            fail_testcase_names = self.redis_client.lrange(self.FAILED_TESTCASES_NAMES, 0, -1)
            return fail_testcase_names if fail_testcase_names else []
        except Exception as e:
            log.error(f"获取失败用例名称列表失败: {e}")
            return []

    def get_success_testcase_names(self):
        """获取所有成功用例名称列表

        Returns:
            list: 成功用例名称列表
        """
        try:
            success_testcase_names = self.redis_client.lrange(self.SUCCESS_TESTCASES_NAMES, 0, -1)
            return success_testcase_names if success_testcase_names else []
        except Exception as e:
            log.error(f"获取成功用例名称列表失败: {e}")
            return []

    def write_end_time(self):
        """记录测试结束时间"""
        try:
            self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "end_time", str(get_now_time()))
        except Exception as e:
            log.error(f"记录测试结束时间失败: {e}")
            raise

    def modify_running_status(self, status):
        """修改测试运行状态

        Args:
            status: 运行状态值(1:运行中, 0:已停止)
        """
        try:
            self.redis_client.set(self.RUNNING_STATUS, str(status))
        except Exception as e:
            log.error(f"修改测试运行状态失败: {e}")
            raise

    def get_running_status(self):
        """获取测试运行状态

        Returns:
            int: 运行状态值(1:运行中, 0:已停止)
        """
        try:
            status_str = self.redis_client.get(self.RUNNING_STATUS)
            return int(status_str) if status_str is not None and status_str != '' else 0  # type: ignore
        except (ValueError, TypeError) as e:
            log.error(f"获取测试运行状态失败，数据类型转换错误: {e}")
            return 0
        except Exception as e:
            log.error(f"获取测试运行状态失败: {e}")
            return 0
