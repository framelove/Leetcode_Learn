#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not (re.match(p, s)):
            return "false"
        elif re.match(p, s).group()!=s:
            return 'false'
        else:
            return 'true'

s = "ab"
p = ".*"
q = Solution()
print(q.isMatch(s,p))
