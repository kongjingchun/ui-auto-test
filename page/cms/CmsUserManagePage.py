# encoding: utf-8
# @File  : CmsUserManagePage.py
# @Author: 孔敬淳
# @Date  : 2025/12/26/14:11
# @Desc  :
import requests
from flask import Config

from base.cms.CmsUserManageBase import CmsUserManageBase
from common.yaml_config import GetConf
from logs.log import log


class CmsUserManage(CmsUserManageBase):
    """CMS用户管理类

    继承UserManageBase类，提供CMS用户管理相关的页面操作方法
    """

    # 接口注册CMS用户
    def register_cms_user(self, user):
        """注册CMS用户"""
        username, password = GetConf().get_user_info(user, "username", "password")
        log.info("api注册cms用户:用户名：" + username + "密码：" + password)
        data = {
            "username": str(username),
            "password": str(password)
        }
        url = GetConf().get_url()
        res = requests.post(url + "api/auth/register", json=data)
        response_data = res.json()
        
        # 判断返回结果中是否包含"注册成功"
        if "注册成功" in str(response_data):
            log.info(f"用户 {username} 注册成功")
            return True
        else:
            error_msg = f"用户 {username} 注册失败，返回结果：{response_data}"
            log.error(error_msg)
            raise Exception(error_msg)


if __name__ == '__main__':
    res = CmsUserManage().register_cms_user("dean_cms")

