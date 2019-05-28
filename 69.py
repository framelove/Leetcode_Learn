#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-28 11:44
# 作者:   ljk

# 整数x的平方根取整
# 个人思路：从0开始遍历，直到x*x>这个数为止【效率低】  o(n)
# 答案思路：用二分法来找 o(logn)【默认是有序的】
class Solution(object):
    def mySqrt(self,x):
        left =0
        right = x
        mid = (left+right)//2
        while (left<=right):
            if (mid*mid<x):
                left = mid+1
                mid = (left+right)//2
            else:
                right = mid-1
                mid = (left + right) // 2
        return right+1




    def mySqrt1(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while(i*i<=x):
            i+=1
        return i-1
a = Solution()
print(a.mySqrt(1))