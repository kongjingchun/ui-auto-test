# encoding: utf-8
# @File  : process_redis.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/18:06
# @Desc  : 测试进度管理类，通过Redis记录测试执行进度

from common.tools import get_now_time
from common.redis_operation import RedisOperation


class Process:
    """测试进度管理类，使用Redis存储测试执行进度和结果"""
    
    def __init__(self):
        """初始化Redis客户端和键名"""
        self.redis_client = RedisOperation().redis_client
        self.UI_AUTOTEST_PROCESS = "ui_autotest_process"      # 进度信息键
        self.FAILED_TESTCASES_NAMES = "failed_testcase_name"  # 失败用例键
        self.SUCCESS_TESTCASES_NAMES = "success_testcase_name"  # 成功用例键
        self.RUNNING_STATUS = "running_status"                # 运行状态键

    def reset_all(self):
        """清空所有进度数据"""
        self.redis_client.delete(self.UI_AUTOTEST_PROCESS)
        self.redis_client.delete(self.FAILED_TESTCASES_NAMES)
        self.redis_client.delete(self.SUCCESS_TESTCASES_NAMES)

    def init_process(self, total):
        """初始化测试进度
        
        Args:
            total: 测试用例总数
        """
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "total", total)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "success", 0)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "fail", 0)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "start_time", str(get_now_time()))
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "end_time", "")
        self.redis_client.set(self.RUNNING_STATUS, 1)

    def update_success(self):
        """成功用例数+1"""
        self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "success")

    def update_fail(self):
        """失败用例数+1"""
        self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "fail")

    def insert_into_fail_testcase_names(self, fail_testcase_name):
        """记录失败用例名称
        
        Args:
            fail_testcase_name: 失败的测试用例名称
        """
        self.redis_client.lpush(self.FAILED_TESTCASES_NAMES, fail_testcase_name)
    
    def insert_into_success_testcase_names(self, success_testcase_name):
        """记录成功用例名称
        
        Args:
            success_testcase_name: 成功的测试用例名称
        """
        self.redis_client.lpush(self.SUCCESS_TESTCASES_NAMES, success_testcase_name)

    def get_result(self):
        """获取测试结果统计
        
        Returns:
            tuple: (总数, 成功数, 失败数, 开始时间)
        """
        total = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "total")
        if total is None:
            total = 0
        success = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "success")
        if success is None:
            success = 0
        fail = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "fail")
        if fail is None:
            fail = 0
        start_time = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "start_time")
        if start_time is None:
            start_time = '-'
        return total, success, fail, start_time

    def get_process(self):
        """计算测试进度百分比
        
        Returns:
            str: 进度百分比，如"50.0%"
        """
        total, success, fail, _ = self.get_result()
        if total == 0:
            return 0
        else:
            return "%.1f" % ((int(success) + int(fail)) / int(total) * 100) + "%"

    def get_fail_testcase_names(self):
        """获取所有失败用例名称列表
        
        Returns:
            list: 失败用例名称列表
        """
        fail_testcase_names = self.redis_client.lrange(self.FAILED_TESTCASES_NAMES, 0, -1)
        return fail_testcase_names
    
    def get_success_testcase_names(self):
        """获取所有成功用例名称列表
        
        Returns:
            list: 成功用例名称列表
        """
        success_testcase_names = self.redis_client.lrange(self.SUCCESS_TESTCASES_NAMES, 0, -1)
        return success_testcase_names

    def write_end_time(self):
        """记录测试结束时间"""
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "end_time", str(get_now_time()))

    def modify_running_status(self, status):
        """修改测试运行状态
        
        Args:
            status: 运行状态值(1:运行中, 0:已停止)
        """
        self.redis_client.set(self.RUNNING_STATUS, status)
