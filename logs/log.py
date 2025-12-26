# 日志配置文件
# 用于生成和管理测试日志

import logging
import os.path
import time

from common.tools import get_project_path, sep


def get_log(logger_name):
    """创建并配置日志对象
    
    Args:
        logger_name: 日志记录器名称
    
    Returns:
        配置好的logger对象
    """
    # 创建日志对象
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # 避免重复添加handler
    if logger.handlers:
        return logger

    # 获取当前时间作为日志文件名
    rq = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    # 日志保存路径
    all_log_path = get_project_path() + sep(["logs", "all_logs"], add_sep_before=True, add_sep_after=True)
    # 目录不存在则创建
    os.makedirs(all_log_path, exist_ok=True)
    # 完整的日志文件路径
    all_log_name = all_log_path + rq + ".log"

    # 创建文件处理器（支持UTF-8编码）
    fh = logging.FileHandler(all_log_name, encoding='utf-8')
    fh.setLevel(logging.INFO)

    # 设置日志格式：时间-文件-模块-函数-行号-级别-消息
    all_log_formatter = logging.Formatter(
        "%(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s ————————- %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")
    # 应用日志格式
    fh.setFormatter(all_log_formatter)

    # 添加处理器到日志对象
    logger.addHandler(fh)
    return logger


# 创建全局日志对象
log = get_log("自动化测试")

if __name__ == '__main__':
    # 测试不同级别的日志输出
    log.debug("调试信息")
    log.info("普通信息")
    log.warning("警告信息")
    log.error("错误信息")
    log.critical("严重错误")
