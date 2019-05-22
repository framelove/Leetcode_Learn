#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-21 14:27
# 作者:   ljk

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r = re
        jin = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            r.next = ListNode((jin +x+y)%10)
            r = r.next
            jin =(jin +x+y)//10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if jin >0:
            r.next = ListNode(jin)
        return re.next



