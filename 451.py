# -*- coding: utf-8 -*-
# Auth： ljk
# E-mail: ljk13572@163.com
# Time： 2021/7/3 11:28
# Software:  PyCharm
'''

用字典保存每个字符的出现次数

将字典按值降序排序

拼接字符串

'''
class Solution:
    def frequencySort(self, s: str) -> str:
        dc = {}
        for i in s:
            dc.setdefault(i, 0)
            dc[i] += 1
        a = sorted(dc.items(), key=lambda item: item[1], reverse=True)

        ss = ''
        for j in a:
            ss += j[0] * j[1]

        return ss

if __name__ == '__main__':
    print(Solution().frequencySort('avcc'))
