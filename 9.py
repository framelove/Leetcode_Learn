#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-13 17:25
# 作者:   ljk

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        
        """
        if x < 0:
            return 'false'
        a = self.get_wei(x)
        aa = a//2
        y = 0
        for i in range(1,aa+1):
            y += x%(10**(i))*10**(a-i)
        xx = (x//(10**(a-aa)))*(10**(a-aa))
        if y == xx:
            return 'true'
        else:
            return 'false'


    def get_wei(self,x):
        i = 0
        while x>10**i:
            i = i+1
        return i


a = Solution()
print(a.isPalindrome(-121))
