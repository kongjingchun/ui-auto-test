#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import sys

TEMPLATE = '''# encoding: utf-8
# @File  : {filename}
# @Author: kongjingchun
# @Date  : {datetime}
# @Desc  :
'''

def main():
    if len(sys.argv) < 2:
        print("用法: python new_py.py 文件名.py")
        return

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        filename += ".py"

    if os.path.exists(filename):
        print(f"文件已存在: {filename}")
        return

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = TEMPLATE.format(
        filename=os.path.basename(filename),
        datetime=now
    )

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"已创建文件: {filename}")


if __name__ == "__main__":
    main()