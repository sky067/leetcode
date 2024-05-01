# -*- coding: utf-8 -*-
# @File    : 303.py.py
# @Des     :

"""
303. 区域和检索 - 数组不可变
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        # 初始化前缀和数组
        self.num_sum = [0] * (len(nums)+1)  # num_sum[0]不存元素
        for i in range(1, len(nums) + 1):
            # num_sum[1] 表示第 0 个元素的前缀和
            # num_sum[i] 表示第 i-1 个元素的前缀和
            self.num_sum[i] = self.num_sum[i-1] + nums[i-1]
        print(self.num_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.num_sum[right+1] - self.num_sum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)