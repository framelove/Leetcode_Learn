#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-22 10:13
# 作者:   ljk

# 无重复字符的最长字串
# 个人思路： 1.无重复、2.最长字串（连续的）\ 两次循环会有超出时间限制的问题
# 答案思路1： 利用一次循环来遍历字符串，如果重复，就从重复字符的位置再遍历
# 答案思路2： 利用一次循环来遍历字符串，但与1不同的是，当有重复字符时，把记录字串的重复字符之前的都给删掉，这样就避免了重复的遍历字符串。
class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        i = 0
        while i< len(s)-max:
            ss = s[i]
            x =0
            for j in range(i+1,len(s)):

                if s[j] not in ss:
                    ss+=s[j]
                else:
                    x = ss.index(s[j])
                    break
            i = i+x+1
            if len(ss)>max:
                max=len(ss)
        return max


    def lengthOfLongestSubstring1(self, s):
        dic={}
        start=0
        m=0
        while(start<=len(s)-1):
            if s[start] not in dic:
                dic[s[start]]=start
                start += 1
            else:
                m=max(m,len(dic))
                start=dic[s[start]]+1
                dic={}
                continue

        m=max(m,len(dic))
        return m


    class Solution(object):
        def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """
            max_num = 0
            num = 0
            str = ' '
            for i in s:
                if i not in str:
                    str += i
                    num += 1
                else:
                    if num > max_num:
                        max_num = num
                    index = str.index(i)
                    str = str[(index + 1):] + i
                    num = len(str)
            if num > max_num:
                max_num = num
            return max_num

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_num =0
        num = 0
        str = ' '
        for i in s:
            if i not in str:
                str +=i
                num +=1
            else:
                if num >max_num:
                    max_num = num
                index = str.index(i)
                str = str[(index+1):]+i
                num = len(str)
        if num>max_num:
            max_num = num
        return max_num
q = Solution()
print(q.lengthOfLongestSubstring("abacd"))
