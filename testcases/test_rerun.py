# encoding: utf-8
# @File  : test_rerun.py
# @Author: kongjingchun
# @Date  : 2025/12/18/19:00
# @Desc  :
import random
import pytest

class TestRerun:
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_rerun(self):
        num = random.randint(1, 5)
        print("num:" + str(num))
        if num != 1:
            print("测试失败+")
            raise Exception("出错了")
        else:
            print("测试成功")
