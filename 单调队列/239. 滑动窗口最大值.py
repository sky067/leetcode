# -*- coding: utf-8 -*-
# @File    : 239. 滑动窗口最大值.py
# @Des     :
from typing import List


# 解法1

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列

        from collections import deque
        # 双端队列，左边为队头，右边为队尾
        queue = deque()
        res = []
        for i, x in enumerate(nums):
            # 第一个窗口的值入队，此时窗口长度少一个，放在后面处理
            if i < k - 1:
                while queue and x > queue[-1]:
                    queue.pop()
                queue.append(x)
            else:
                while queue and x > queue[-1]:
                    queue.pop()
                queue.append(x)

                # 窗口长度满足开始，记录当前窗口最大值
                res.append(queue[0])

                # 移除离开窗口的元素
                if queue[0] == nums[i - k + 1]:
                    queue.popleft()

        return res


# 方法二
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列

        from collections import deque
        # 双端队列，左边为队头，右边为队尾
        queue = deque()  # 存下标
        res = []
        for i, x in enumerate(nums):

            # 入队之前删除较小值
            while queue and nums[queue[-1]] < x:
                queue.pop()
            queue.append(i)

            # 离开窗口的值出队
            while queue[0] < i - k + 1:
                queue.popleft()

            # 当 i 满足第一个窗口后，开始记录答案
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1,3,-1,-3,5,3,6]
    print(s.maxSlidingWindow(nums))