#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
datetime:2019-05-07 20:07
author:ljk
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        i = 1
        max = len(nums)
        # 遍历整个数组，交换遍历所到之处i与j+1处的值
        while i < max:
            if nums[i]>nums[j]:
                a = nums[j+1]
                nums[j+1] = nums[i]
                nums[i] = a
                j+=1
            i+=1
        return j+1

