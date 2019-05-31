#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-31 15:29
# 作者:   ljk

# 二叉树的所有路径
# 个人思路：dfs遍历二叉树

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        def dg(node,res,s):
            if node.left == None and node.right ==None:
                s+=str(node.val)
                res.append(s)
                return
            s+=str(node.val)+'->'
            if node.left:
                dg(node.left,res,s)
            if node.right:
                dg(node.right,res,s)
        dg(root,res,'')
        return res


