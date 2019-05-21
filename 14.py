#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-21 9:44
# 作者:   ljk

# 测试用例要广而全

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a={}
        w =''
        lens = len(strs)
        if lens == 0:
            return w


        len1 = len(strs[0])
        for i,j in enumerate(strs[0]):
            a[i] =j
        for x in range(1,len(strs)):
            for i,j in enumerate(strs[x]):
                if i < len1:
                    a[i]+=j
        for i,j in enumerate(strs[0]):
            if a[i] == j*lens:
                continue
            else:
                return strs[0][:i]
        return strs[0]
q = Solution()
print(q.longestCommonPrefix(["c",'c']))
