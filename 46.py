#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dfs递归实现
# 参考网址
# https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51534048

import itertools
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        max = len(nums)
        def dg(res,l,r,n,max):
            if n == max:
                print(l)
                res.append(l)
            for i in range(0,len(r)):
                dg(res,l+[r[i]],r[:i]+r[i+1:],n+1,max)
        dg(res,[],nums,0,max)
        return res
    def permute1(self,nums):
        return [list(i) for i in itertools.permutations(nums,len(nums))]







a = [1,2,3]
q = Solution()
print(q.permute1(a))
