# -*- coding: utf-8 -*-
# @File    : 76最小覆盖子串.py
# @Des     :
from math import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        from collections import defaultdict

        need = defaultdict(int)
        for i in t:
            need[i] += 1

        window = defaultdict(int)
        left, right = 0, 0
        valid = 0
        start, length = 0, float(inf)
        while right < len(s):

            c = s[right]
            window[c] += 1
            right += 1  # 左闭右开

            if c in need:
                if window[c] == need[c]:
                    valid += 1

                    # 缩小窗口
                    while valid == len(need):

                        # 记录最小窗口
                        if right - left < length:
                            start = left
                            length = right - left

                        d = s[left]  # 离开窗口
                        left += 1  # 缩小窗口
                        # 窗口内数据更新
                        if d in need:
                            if window[d] == need[d]:
                                valid -= 1
                        window[d] -= 1

        return '' if length == float(inf) else s[start:length + start]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    res = Solution().minWindow(s, t)
    print(res)