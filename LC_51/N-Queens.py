"""
The NQueens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You 
may return the answer in any order.

Each solution contains a distinct board configuration of the NQueens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""
from typing import List
from common_funcs import listToString


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(board: List[List[str]], row: int) -> None:
            if row == n:
                res.append([''.join(row) for row in board])
                return 
            for col in range(n):
                if validNQueens(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row + 1)
                    board[row][col] = '.'
        
        def validNQueens(board: List[str], row: int, col: int) -> bool:
            for i in range(row):
                if board[i][col] == 'Q':  # check top
                    return False
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
                if board[i][j] == 'Q':  # check top right
                    return False
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 'Q':  # check top left
                    return False
            return True

        backtrack([['.'] * n for _ in range(n)], 0)
        return res


def main():
    while True:
        try:
            line = input()
            n = int(line)

            sol = Solution()
            ret = sol.solveNQueens(n)

            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
