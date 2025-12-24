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

    def get_username_password(self, user):
        """获取用户名和密码"""
        return self.env["user"][user]["username"], self.env["user"][user]["password"]

    def get_url(self):
        """获取URL地址"""
        return self.env["url"]

    def get_mysql_config(self):
        """获取MySQL配置"""
        return self.env["mysql"]

    def get_redis_config(self):
        """获取Redis配置"""
        return self.env["redis"]


if __name__ == '__main__':
    print(GetConf().get_redis_config())
