# encoding: utf-8
# @File  : test_assert.py
# @Author: kongjingchun
# @Date  : 2025/12/18/19:29
# @Desc  :

from pytest_assume.plugin import assume


class TestAssert:
    def test_assert(self):
        # 使用assume断言保证测试用例执行(1+1==3时生效)
        assume(1 + 1 == 2)
        a = 2
        b = 2
        assert a == b
        print("over")
