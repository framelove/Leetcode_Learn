#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-19 10:46
# 作者:   ljk

# 括号生成
# 个人思路： 先生成各种可能的组合，然后调用20判断有效性的函数(错）
#           题中只涉及小括号，所以只要左括号>右括号即可
import itertools
class Solution(object):
    # 超出时间限制
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ls = ['(',')']*3
        res = []
        for i in itertools.permutations(ls,len(ls)):
            s = ""
            for ii in list(i):
                s += ii
            if s not in res and self.isValid(s):
                res.append(s)
        return res
    def isValid(self,s):
        x = 0
        y = 0
        for i in s:
            if i == '(':
                x+=1
            if i == ")":
                y+=1
            if y>x:
                return False
        return True







    # 递归DFS+剪枝
    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dg(left,right,n,s):
            if left == n and right == n:
                res.append(s)
            if left<n:
                dg(left+1,right,n,s+'(')
            if left > right:
                dg(left,right+1,n,s+')')
        dg(0,0,n,'')
        return res


a = Solution()
print(a.generateParenthesis1(3))
