"""
Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
"adjacent" cells are horizontally or vertically neighboring. The same letter
cell may not be used more than once.
"""
from typing import List
from common_funcs import stringToList, stringToString


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(board, word, row, col, x):
            """
            row: the current row
            col: the current column
            x: the current index of letter to be matched in word
            """
            if x == len(word):  # if current index exceeds word length
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                # if current row/col exceeds the board boundaries
                return False
            if board[row][col] != word[x]:
                # if the letter does not match the current letter in word
                return False
            char = board[row][col]  # first char found, check remaining part
            board[row][col] = " "  # avoid re-visits
            # check all 4 neighbors with the rest of the word
            res = dfs(board, word, row+1, col, x+1) or \
                  dfs(board, word, row, col+1, x+1) or \
                  dfs(board, word, row-1, col, x+1) or \
                  dfs(board, word, row, col-1, x+1)
            board[row][col] = char  # restore the char
            return res
        
        # find word starting from all positions
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j, 0):
                    return True
        return False


def main():
    while True:
        try:
            line = input()
            board = stringToList(line)
            line = input()
            word = stringToString(line)
            
            sol = Solution()
            ret = sol.exist(board, word)
            
            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
