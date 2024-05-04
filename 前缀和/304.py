# -*- coding: utf-8 -*-
# @File    : 304.py
# @Des     :

"""
304. 二维区域和检索 - 矩阵不可变
https://leetcode.cn/problems/range-sum-query-2d-immutable/description/
"""

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.region_sum = self.init_region(matrix)
        # print(self.region_sum)

    # 初始化二维前缀和数组，第一行第一列不存值
    def init_region(self, matrix):
        row_num, column_num = len(matrix), len(matrix[0])  # 行，列数

        region_sum = [[0] * (column_num + 1) for _ in range(row_num + 1)]

        for i in range(1, row_num + 1):
            for j in range(1, column_num + 1):
                region_sum[i][j] = region_sum[i][j - 1] + region_sum[i - \
                    1][j] - region_sum[i - 1][j - 1] + matrix[i - 1][j - 1]

        return region_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.region_sum[row2 + 1][col2 + 1] - \
            self.region_sum[row1][col2 + 1] - self.region_sum[row2 + 1][col1] + \
            self.region_sum[row1][col1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
