"""

438. 找到字符串中所有字母异位词
https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        from collections import defaultdict

        window, need = defaultdict(int), defaultdict(int)

        # 初始化 need, 子串中相同字符 +1
        for i in p:
            need[i] += 1

        left, right = 0, 0   # 左闭右开窗口
        valid = 0  # 记录窗口中字符数满足对应子串字符数的个数

        res = []
        # 创建窗口
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1

                # 窗口内此字符数量是否达到要求
                if window[c] == need[c]:
                    valid += 1

            # 当窗口长度大于子串长度时，收缩窗口, 同时判断窗口内元素是否满足子串要求
            while (right - left) == len(p):
                if valid == len(need):
                    res.append(left)

                # 窗口内数据更新
                d = s[left]
                if d in window:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

                left += 1

        return res


if __name__ == '__main__':
    s = 'cbaebabacd'
    p = 'abc'
    r = Solution().findAnagrams(s, p)
    print(r)