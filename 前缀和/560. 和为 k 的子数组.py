# -*- coding: utf-8 -*-
# @File    : 560. 和为 k 的子数组.py
# @Des     :
from typing import List

"""

前缀和 + 哈希表
"""
class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        sums = [0] * (len(nums) + 1)  # 前缀和数组
        sums_map = defaultdict(int)  # 前缀和 map, 记录前缀和出现的次数
        sums_map[0] = 1
        count = 0

        for i in range(len(nums)):
            sums[i + 1] = sums[i] + nums[i]  # 构建前置和

            # 当前前缀和
            cur_sum = sums[i + 1]
            # 计算 map 中 cur_sum -k 的个数, 即子数组和为 k 的个数
            count += sums_map[cur_sum - k]

            # 将前缀和加入 map, 需在统计k的个数后, 最后加入map
            sums_map[cur_sum] += 1

        return count

