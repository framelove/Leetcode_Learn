#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-16 9:48
# 作者:   ljk

# 整数转罗马数字
# 个人思路：将整数转为字符串；将各个分位的数用罗马数字表示；拼接起来
# 改进思路： 不用将整数转为字符串，直接整出如1000，然后建立千分位的列表，利用索引与整除的关系

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        a = {'1':'I', '2':'II', '3':'III', '4':'IV', '5':'V',
             '6':'VI', '7':'VII', '8':'VIII', '9':'IX', '10':'X',
             '20':'XX', '30':'XXX', '40':'XL', '50':'L', '60':'LX',
             '70':'LXX', '80':'LXXX', '90':'XC', '100':'C', '200':'CC',
             '300':'CCC', '400':'CD', '500':'D', '600':'DC', '700':'DCC',
             '800':'DCCC', '900':'CM', '1000':'M', '2000':'MM', '3000':'MMM',
             '000':'','00':'','0':''
             }
        lm = ''
        if num<=0 or num>3999:
            return None
        lens = len(str(num))
        for i,j in enumerate(str(num)):
            s = j+"0"*(lens-i-1)
            lm += a[s]
        return lm

    def intToRoman1(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10];
s = Solution()

print(s.intToRoman(70))