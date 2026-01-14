# 日志配置文件
# 用于生成和管理测试日志

import logging
import os.path
import sys
import time

from common.tools import get_project_path, sep


def _should_create_log_file():
    """判断是否应该创建log文件
    
    在IDE编辑时，通常pytest只是进行代码检查（--collect-only），不应该创建log文件。
    只有在真正执行测试时才创建log文件。
    
    Returns:
        bool: 如果应该创建log文件返回True，否则返回False
    """
    # 检查命令行参数中是否有--collect-only或--co（只收集不执行）
    if '--collect-only' in sys.argv or '--co' in sys.argv:
        return False
    
    # 检查是否在pytest环境中
    # 如果pytest模块没有被导入，说明不在测试环境中，不创建log文件
    if 'pytest' not in sys.modules:
        return False
    
    # 尝试检查pytest的配置对象
    # 如果是在IDE编辑时，通常不会有活动的pytest session或config对象
    try:
        import pytest
        # 如果pytest的_config对象存在且collectonly为True，说明只是收集不执行
        if hasattr(pytest, '_config') and pytest._config:
            if hasattr(pytest._config.option, 'collectonly') and pytest._config.option.collectonly:
                return False
    except Exception:
        # 如果无法检查，默认不创建（保守策略）
        pass
    
    return True


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

    # 检查是否应该创建log文件（避免在IDE编辑时创建）
    if not _should_create_log_file():
        # 只添加一个NullHandler，避免"No handlers could be found"警告
        logger.addHandler(logging.NullHandler())
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
