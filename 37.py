#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-14 13:48
# 作者:   ljk
# 解数独

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.solve(board)
    def solve(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in ["1","2","3","4","5","6","7","8","9"]:
                        board[i][j] = c
                        if not self.isValid(board):
                            board[i][j] = '.'
                            continue
                        if self.solve(board):
                            return True
                        else:
                            board[i][j] = '.'
                    return False
        return True

    def isValid(self,board):
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


a = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
A = Solution()
print(A.solveSudoku(a))
print(a)



