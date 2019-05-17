#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-17 17:36
# 作者:   ljk

# 有效的括号
# 个人思路：后进先出，栈的思路
# 答案思路：直接在一次次的循环中replace掉一个完整的括号，最后看字符串是否为空
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        a ={'(':')','[':']','{':'}'}
        x,y = 0,0
        zuo = []
        for j,i in enumerate(s):
            if i in a.keys():
                zuo.append(i)
                x += 1
            else:
                y += 1
                if y > x:
                    return False
                elif a[zuo[-1]] == i:
                    zuo.pop()# 删除列表的最后一个元素
                else:
                    return False
        if not zuo:
            return True


    def isValid1(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''










a =Solution()
print(a.isValid("[(({})}]"))

