#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-9 14:37
# 作者:   ljk

# 参考网上想法，从外到内一层一层的来转
import math
class Solution:
    def rotate(self, matrix):
        lens = len(matrix)-1
        a = math.ceil((lens+1)/2)
        for i in range(a):
            for j in range(i,lens-i):

                matrix[j][lens - i], matrix[lens - i][lens - j], matrix[lens - j][i],matrix[i][j]= \
                    matrix[i][j], matrix[j][lens - i], matrix[lens - i][lens - j], matrix[lens - j][i]



matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s = Solution()
s.rotate(matrix)
print(matrix)