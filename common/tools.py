# encoding: utf-8
# @File  : tools.py
# @Author: kongjingchun
# @Date  : 2025/11/28/18:30
# @Desc  : 工具类，提供常用的功能函数

import datetime
import os
from pathlib import Path
from typing import List, Union


def get_now_time() -> datetime.datetime:
    """
    获取当前时间

    Returns:
        datetime.datetime: 当前的日期时间对象
    """
    return datetime.datetime.now()


def get_project_path(levels_up: int = 2) -> str:
    """
    获取项目根路径
    通过当前文件的绝对路径，向上指定级数目录获取项目根路径
    Args:
        levels_up (int): 向上几级目录，默认为2
    Returns:
        str: 项目根目录的绝对路径
    """
    current_file = Path(__file__).resolve()
    project_path = current_file.parents[levels_up - 1]
    return str(project_path)


def sep(path: Union[List[str], tuple], add_sep_before: bool = False,
        add_sep_after: bool = False) -> str:
    """
    构造路径字符串，在路径片段之间添加系统分隔符
    Args:
        path: 路径片段列表或元组
        add_sep_before: 是否在路径前添加分隔符，默认为False
        add_sep_after: 是否在路径后添加分隔符，默认为False
    Returns:
        str: 处理后的路径字符串
    Example:
        >>> sep(['dir1', 'dir2', 'file.txt'])
        'dir1/dir2/file.txt'
        >>> sep(['dir1', 'dir2'], add_sep_before=True, add_sep_after=True)
        '/dir1/dir2/'
    """
    # 使用 os.path.join 更安全，能正确处理不同操作系统的路径
    all_path = os.path.join(*path)

    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep

    return all_path


def get_img_path(img_name):
    return get_project_path() + sep(['img', img_name], add_sep_before=True)



if __name__ == '__main__':
    # 测试函数功能
    print(get_img_path('机器猫.img'))

