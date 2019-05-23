#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-23 9:57
# 作者:   ljk

# 个人思路：再o(log(m+n))下，将两个数组按大小合并，然后再取中位数
# 方法1没有达到时间复杂度的要求


# 个人思路2：在不对两个数组排序的前提下，可以用二分查找来找到中位数(不会，留坑）

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        pass












    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        i = 0
        j = 0
        while len(nums)< len(nums1)+len(nums2):
            if i < len(nums1) and j<len(nums2):
                if nums1[i]<nums2[j]:
                    nums.append(nums1[i])
                    i+=1
                else:
                    nums.append(nums2[j])
                    j+=1
            elif i == len(nums1):
                nums+=nums2[j:]
            else:
                nums += nums1[i:]
        if len(nums) %2 ==1:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2]+nums[(len(nums)//2)-1])/2



s = Solution()
print(s.findMedianSortedArrays([1,2],[3,4]))
