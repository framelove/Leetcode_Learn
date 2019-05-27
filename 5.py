#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-27 9:55
# 作者:   ljk

# 最长回文字串
# 个人思路：用递归来生成字串（需要连续，所以只能删除两头的元素），然后逐个判断是否回文===》超出时间限制
# 答案思路：动态规划实现


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 使用动态规划，用空间换时间，把问题拆分
        # 获取字符串s的长度
        str_length = len(s)
        # 记录最大字符串长度
        max_length = 0
        # 记录位置
        start = 0
        # 循环遍历字符串的每一个字符
        for i in range(str_length):
            # 如果当前循环次数-当前最大长度大于等于1  并  字符串[当前循环次数-当前最大长度-1:当前循环次数+1]  == 取反后字符串
            if i - max_length >= 1 and s[i - max_length - 1: i + 1] == s[i - max_length - 1: i + 1][::-1]:
                # 记录当前开始位置
                start = i - max_length - 1
                # 取字符串最小长度为2，所以+=2，s[i-max_length-1: i+1]
                max_length += 2
                continue
            # 如果当前循环次数-当前最大长度大于等于0  并  字符串[当前循环次数-当前最大长度:当前循环次数+1]  == 取反后字符串
            if i - max_length >= 0 and s[i - max_length: i + 1] == s[i - max_length: i + 1][::-1]:
                start = i - max_length
                # 取字符串最小长度为1，所以+=1，s[i-max_length: i+1]
                max_length += 1
        # 返回最长回文子串
        return s[start: start + max_length]



    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        lens = len(s)
        a={'res':''}
        def dg(dep,s,a):
            if dep == lens-1:
                if len(s) > len(a['res']):
                    a['res'] = s
                return
            if panduan(s):
                if len(s)>len(a['res']):
                    a['res'] = s
                    return

            dg(dep+1,s[1:],a)
            dg(dep+1,s[:-1],a)

        def panduan(s):
            ss = s[::-1]
            if s == ss:
                return True
            else:
                return False
        if not s:
            return ''
        dg(0, s,a)
        return a['res']




a = Solution()
print(a.longestPalindrome1("babaddtattarrattatddetartrateedredividerb"))
