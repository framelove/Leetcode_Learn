#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-14 11:25
# 作者:   ljk


class Solution(object):
    ## 最优答案
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        raw = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        col = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        cell = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

        for i in range(9):
            for j in range(9):
                num = (3 * (i // 3) + j // 3)  # 找单元
                temp = board[i][j]
                if temp != ".":
                    if temp not in raw[i] and temp not in col[j] and temp not in cell[num]:
                        raw[i][temp] = 1
                        col[j][temp] = 1
                        cell[num][temp] = 1
                    else:
                        return False
        return True


    # 自己的解答
    def isValidSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        sum = 0
        for q in board:
            sum+=self.pan_duan(q)
        for w in self.zhuan_zhi(board):
            sum += self.pan_duan(w)
        for e in range(3):
            for r in range(3):
                t = []
                for tt in board[e*3:(e+1)*3]:
                    t+=tt[r*3:(r+1)*3]
                sum += self.pan_duan(t)
        if sum == 0:
            return True
        else:
            return False
    def pan_duan(self,lists):
        for i in range(9):
            for j in range(i+1,9):
                if lists[i] == lists[j] and lists[i]!='.':
                    return 1
        return 0

    def zhuan_zhi(self,a):
        s = []
        for i in range(len(a[0])):
            ss = []
            for j in range(len(a)):
                ss.append(a[j][i])
            s.append(ss)
        return s

a = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

A = Solution()
print(A.isValidSudoku(a))



