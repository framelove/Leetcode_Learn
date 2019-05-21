#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-20 13:58
# 作者:   ljk

# 电话号码的字母组合
# 使用递归成功
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dicts = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        if not digits:
            return []
        def dg(n,lens,s):
            if n == lens:
                res.append(s)
                return
            for i in dicts[digits[n]]:
                dg(n+1,lens,s+i)


        dg(0,len(digits),'')
        return res







a = Solution()
print(a.letterCombinations('368'))
