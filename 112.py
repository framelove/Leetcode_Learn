#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-6-2 13:20
# 作者:   ljk

# 路径总和
# 将列表转化为一颗完全二叉树

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Tree(object):
    def __init__(self):
        self.root = None

    def construct_tree(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dg(root,sum_1,s):
            if root and root.left == None and root.right ==None:
                if sum_1 == sum:
                    s.append(1)
            if root.left:
                dg(root.left,sum_1+root.left.val,s)
            if root.right:
                dg(root.right,sum_1+root.right.val,s)
        if not root:
            return False
        s =[]
        dg(root,root.val,s)
        if len(s)>0:
            return True
        else:
            return False

    def hasPathSum1(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return (self.hasPathSum1(root.left,sum-root.val) or (self.hasPathSum(root.right,sum-root.val)))

a = Tree()
a.construct_tree([5,4,8,11,'',13,4,7,2,'','','',1])
b = Solution()
print(b.hasPathSum1(a.root,22))
