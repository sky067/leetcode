# -*- coding: utf-8 -*-
# @File    : 53最大字数组和.py
# @Des     :
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        # dp[i] = max((dp[i-1] + nums[i]), nums[i])
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max((dp[i - 1] + nums[i]), nums[i])

        return max(dp)


if __name__ == '__main__':
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))
