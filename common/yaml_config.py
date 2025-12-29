# encoding: utf-8
# @File  : yaml_config.py
# @Author: 孔敬淳
# @Date  : 2025/11/28/16:54
# @Desc  : YAML配置文件读取类
import yaml
from typing import Any, Optional, Dict, Tuple
from common.tools import get_project_path, sep


class GetConf:
    """配置文件读取类"""

    def __init__(self):
        """初始化并加载环境配置文件"""
        # 读取环境配置文件
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_user_info(self, user: str, *fields: str) -> Any:
        """
        获取用户信息
        :param user: 用户标识
        :param fields: 要获取的字段名，如 'username', 'password', 'email', 'phone' 等
        :return: 如果传入多个字段，返回元组；如果传入单个字段，返回该字段值；如果不传字段，返回整个用户字典
        """
        user_data = self.env["user"][user]
        
        if not fields:
            # 如果没有指定字段，返回整个用户信息字典
            return user_data
        elif len(fields) == 1:
            # 如果只有一个字段，返回单个值
            return user_data.get(fields[0])
        else:
            # 如果有多个字段，返回元组
            return tuple(user_data.get(field) for field in fields)
    
    def get_username_password(self, user: str) -> Tuple[str, str]:
        """获取用户名和密码（向后兼容的便捷方法）"""
        return self.get_user_info(user, "username", "password")

    def get_school_name(self):
        """获取学校名称"""
        return self.env["school_name"]

    def get_url(self):
        """获取URL地址"""
        return self.env["url"]

    def get_mysql_config(self):
        """获取MySQL配置"""
        return self.env["mysql"]

    def get_redis_config(self):
        """获取Redis配置"""
        return self.env["redis"]

    def get_dingding_webhook(self):
        """获取钉钉WebHook地址"""
        return self.env["dingding_group"]["webhook"]

    def get_jenkins_url(self):
        """获取jenkins地址"""
        return self.env["jenkins"]


if __name__ == '__main__':
    print(GetConf().get_user_info("dean"))
