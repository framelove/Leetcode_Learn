#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-29 9:31
# 作者:   ljk

# 个人思路：一次循环来判断(X)   题目不要求是连续子序列


# 答案思路： 贪心算法。
# res储存当前的最佳升序列（即满足res[1]>res[0]的条件下，res[1]越小越佳），
# min储存当前的最小元素。
# min不等于res[0]时，扫描到某个元素小于res[1]时更新res，
# min等于res[0]时更新res[1]。

# float('inf')表示无穷大
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res=[]
        if len(nums)<3:
            return False
        min = nums[0]
        res.append(nums[0])
        for i in nums:
            if i< min:
                min = i
                if len(res) ==1:
                    res[0]=i
                continue
            if i>res[-1]:
                res.append(i)
            if len(res) ==2 and i<res[-1] and i> res[-2]:
                res[-1] = i
            if len(res) == 2 and res[0]>min and i<res[1]:
                res[0] = min
                res[1] = i
            if len(res)>2:
                return True
        return False

    def increasingTriplet1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        minnum=float('inf')
        maxnum=float('inf')
        for num in nums:
            if num<minnum:
                minnum=num
            elif minnum<num<=maxnum:
                maxnum=num
            elif maxnum<num:
                return True
        return False








a = Solution()
print(a.increasingTriplet1([3,4,1,2,3]))
# [3,4,1,5]

