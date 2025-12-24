# encoding: utf-8
# @File  : redis_operation.py
# @Author: kongjingchun
# @Date  : 2025-12-24 16:33:18
# @Desc  : Redis数据库操作封装类

import redis

from common.yaml_config import GetConf


class RedisOperation:
    """Redis操作类，用于连接和操作Redis数据库"""
    
    def __init__(self):
        """初始化Redis连接"""
        # 从配置文件获取Redis连接信息
        redis_info = GetConf().get_redis_config()
        # 创建Redis客户端连接
        self.redis_client = redis.Redis(
            host=redis_info["host"],        # Redis服务器地址
            port=redis_info["port"],        # Redis端口
            db=redis_info["db"],            # 数据库编号
            decode_responses=True,          # 自动解码响应为字符串
            encoding="UTF-8"                # 字符编码格式
            # password=user:password        # 如需密码认证，取消注释并配置
        )


if __name__ == '__main__':
    # 测试Redis连接，获取key为"kjc"的值
    print(RedisOperation().redis_client.get("kjc"))