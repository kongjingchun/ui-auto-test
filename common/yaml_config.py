# encoding: utf-8
# @File  : yaml_config.py
# @Author: kongjingchun
# @Date  : 2025/11/28/16:54
# @Desc  : YAML配置文件读取类
import yaml
from typing import Any, Optional, Dict, Tuple
from common.tools import get_project_path, sep


class GetConf:
    """配置读取类，用于读取YAML格式的配置文件"""

    def __init__(self, config_file: Optional[str] = None):
        """
        初始化配置读取器
        
        Args:
            config_file: 配置文件路径，如果为None则使用默认路径 config/environment.yaml
            
        Raises:
            FileNotFoundError: 配置文件不存在
            yaml.YAMLError: YAML格式错误
        """
        if config_file is None:
            config_file = get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True)

        self.config_file = config_file
        self.env_data: Dict[str, Any] = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """
        加载YAML配置文件
        
        Returns:
            Dict[str, Any]: 配置数据字典
            
        Raises:
            FileNotFoundError: 配置文件不存在
            yaml.YAMLError: YAML格式错误
        """
        try:
            with open(self.config_file, "r", encoding="utf-8") as env_file:
                # 使用 safe_load 更安全，避免执行任意代码
                data = yaml.safe_load(env_file)
                if data is None:
                    raise ValueError(f"配置文件 {self.config_file} 为空")
                return data
        except FileNotFoundError:
            raise FileNotFoundError(f"配置文件不存在: {self.config_file}")
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"YAML格式错误: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """
        获取配置值（通用方法）
        
        Args:
            key: 配置键名，支持点号分隔的嵌套键（如 "database.host"）
            default: 默认值，如果键不存在则返回此值
            
        Returns:
            Any: 配置值，如果不存在则返回默认值
        """
        keys = key.split(".")
        value = self.env_data

        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default

    def get_username_password(self, user) -> Tuple[str, str]:
        """
        获取用户名和密码
        
        Returns:
            Tuple[str, str]: (用户名, 密码)元组
            
        Raises:
            KeyError: 配置文件中缺少username或password字段
        """
        try:
            username = self.env_data["user"][user]["username"]
            password = self.env_data["user"][user]["password"]

            if username is None or password is None:
                missing = []
                if username is None:
                    missing.append("username")
                if password is None:
                    missing.append("password")
                raise KeyError(f"配置文件中缺少必需的字段: {', '.join(missing)}")

            return username, password
        except KeyError as e:
            raise KeyError(f"获取用户名密码失败: {e}")

    def get_url(self) -> str:
        """
        获取URL配置
        
        Returns:
            str: URL地址
            
        Raises:
            KeyError: 配置文件中缺少url字段
        """
        url = self.env_data.get("url")
        if url is None:
            raise KeyError("配置文件中缺少必需的字段: url")
        return url


if __name__ == '__main__':
    print(GetConf().get_username_password("jay"))
