# encoding: utf-8
# @File  : tools.py
# @Author: 孔敬淳
# @Date  : 2025/11/28/18:30
# @Desc  : 工具类，提供常用的功能函数

import datetime
import os
from pathlib import Path
from typing import List, Union

import requests


def get_now_time() -> datetime.datetime:
    """
    获取当前时间
    :return: 当前的日期时间对象
    """
    return datetime.datetime.now()


def get_now_time_str() -> str:
    """
    获取当前时间字符串
    :return: 当前时间字符串
    """
    return get_now_time().strftime("%Y%m%d%H%M%S")


def get_project_path(levels_up: int = 2) -> str:
    """
    获取项目根路径
    :param levels_up: 向上几级目录，默认为2
    :return: 项目根目录的绝对路径
    """
    current_file = Path(__file__).resolve()
    project_path = current_file.parents[levels_up - 1]
    return str(project_path)


def sep(path: Union[List[str], tuple], add_sep_before: bool = False,
        add_sep_after: bool = False) -> str:
    """
    构造路径字符串，在路径片段之间添加系统分隔符
    :param path: 路径片段列表或元组
    :param add_sep_before: 是否在路径前添加分隔符，默认为False
    :param add_sep_after: 是否在路径后添加分隔符，默认为False
    :return: 处理后的路径字符串
    """
    # 使用 os.path.join 更安全，能正确处理不同操作系统的路径
    all_path = os.path.join(*path)

    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep

    return all_path


def get_img_path(img_name):
    """
    获取图片文件的完整路径
    :param img_name: 图片文件名
    :return: 图片文件的完整路径
    """
    return get_project_path() + sep(['img', img_name], add_sep_before=True)


def get_every_wallpaper():
    """
    从bing获取每日壁纸
    :return:
    """
    everyday_wallpaper_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&mkt=zh-CN"
    try:
        res = requests.get(url=everyday_wallpaper_url)
        wallpaper_url = "https://cn.bing.com" + res.json()["images"][0]["url"][:-7]
    except Exception as e:
        print(e)
        wallpaper_url = ""
    return wallpaper_url


if __name__ == '__main__':
    # 测试函数功能
    print(sep(['img', '机器猫.png']))
