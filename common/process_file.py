# encoding: utf-8
# @File  : process_file.py
# @Author: 孔敬淳
# @Date  : 2025/12/31
# @Desc  : 测试进度管理类，通过文件记录测试执行进度

import json
import os
import threading
from common.tools import get_now_time, get_project_path, sep


class Process:
    """测试进度管理类，使用文件存储测试执行进度和结果"""
    
    def __init__(self):
        """初始化文件路径和锁"""
        # 进度文件路径
        self.process_file = get_project_path() + sep(['logs', 'test_process.json'], add_sep_before=True)
        # 失败用例文件路径
        self.failed_file = get_project_path() + sep(['logs', 'failed_testcases.json'], add_sep_before=True)
        # 确保logs目录存在
        logs_dir = os.path.dirname(self.process_file)
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        # 线程锁，确保文件操作的线程安全
        self._lock = threading.Lock()
    
    def _read_json_file(self, file_path):
        """读取JSON文件
        
        Args:
            file_path: 文件路径
            
        Returns:
            dict: JSON数据，如果文件不存在或读取失败返回空字典
        """
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"读取文件失败: {file_path}, 错误: {e}")
            return {}
    
    def _write_json_file(self, file_path, data):
        """写入JSON文件
        
        Args:
            file_path: 文件路径
            data: 要写入的数据
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"写入文件失败: {file_path}, 错误: {e}")
    
    def reset_all(self):
        """清空所有进度数据"""
        with self._lock:
            # 重置进度数据
            process_data = {
                "total": 0,
                "success": 0,
                "fail": 0,
                "start_time": "",
                "end_time": "",
                "running_status": 0
            }
            self._write_json_file(self.process_file, process_data)
            # 清空失败用例列表
            self._write_json_file(self.failed_file, {"failed_testcases": []})
    
    def init_process(self, total):
        """初始化测试进度
        
        Args:
            total: 测试用例总数
        """
        with self._lock:
            process_data = {
                "total": total,
                "success": 0,
                "fail": 0,
                "start_time": str(get_now_time()),
                "end_time": "",
                "running_status": 1
            }
            self._write_json_file(self.process_file, process_data)
    
    def update_success(self):
        """成功用例数+1"""
        with self._lock:
            process_data = self._read_json_file(self.process_file)
            if not process_data:
                process_data = {"total": 0, "success": 0, "fail": 0}
            process_data["success"] = process_data.get("success", 0) + 1
            self._write_json_file(self.process_file, process_data)
    
    def update_fail(self):
        """失败用例数+1"""
        with self._lock:
            process_data = self._read_json_file(self.process_file)
            if not process_data:
                process_data = {"total": 0, "success": 0, "fail": 0}
            process_data["fail"] = process_data.get("fail", 0) + 1
            self._write_json_file(self.process_file, process_data)
    
    def insert_into_fail_testcase_names(self, fail_testcase_name):
        """记录失败用例名称
        
        Args:
            fail_testcase_name: 失败的测试用例名称
        """
        with self._lock:
            failed_data = self._read_json_file(self.failed_file)
            if "failed_testcases" not in failed_data:
                failed_data["failed_testcases"] = []
            # 添加到列表开头（模拟lpush行为）
            failed_data["failed_testcases"].insert(0, fail_testcase_name)
            self._write_json_file(self.failed_file, failed_data)
    
    def get_result(self):
        """获取测试结果统计
        
        Returns:
            tuple: (总数, 成功数, 失败数, 开始时间)
        """
        process_data = self._read_json_file(self.process_file)
        total = process_data.get("total", 0)
        success = process_data.get("success", 0)
        fail = process_data.get("fail", 0)
        start_time = process_data.get("start_time", "-")
        return total, success, fail, start_time
    
    def get_process(self):
        """计算测试进度百分比
        
        Returns:
            str: 进度百分比，如"50.0%"
        """
        total, success, fail, _ = self.get_result()
        if total == 0:
            return "0%"
        else:
            percentage = (int(success) + int(fail)) / int(total) * 100
            return "%.1f%%" % percentage
    
    def get_fail_testcase_names(self):
        """获取所有失败用例名称列表
        
        Returns:
            list: 失败用例名称列表
        """
        failed_data = self._read_json_file(self.failed_file)
        return failed_data.get("failed_testcases", [])
    
    def write_end_time(self):
        """记录测试结束时间"""
        with self._lock:
            process_data = self._read_json_file(self.process_file)
            process_data["end_time"] = str(get_now_time())
            self._write_json_file(self.process_file, process_data)
    
    def modify_running_status(self, status):
        """修改测试运行状态
        
        Args:
            status: 运行状态值(1:运行中, 0:已停止)
        """
        with self._lock:
            process_data = self._read_json_file(self.process_file)
            process_data["running_status"] = status
            self._write_json_file(self.process_file, process_data)

