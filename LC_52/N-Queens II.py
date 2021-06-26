"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens 
puzzle.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Time Complexity : O(n!)
        Space Complexity : O(3n) = O(n)
        columns: if another Queen exists in the column
        diag1: if another Queen exists in the minor diagonal
        diag2: if another Queen exists in the major diagonal
        """
        columns, diag1, diag2 = [False]*n, [False]*2*n, [False]*2*n
        
        def backtrack(row: int, col: List[bool], 
                    diag1: List[bool], diag2: List[bool]) -> int:
            count = 0
            if row == n:
                return 1
            for col in range(n):
                if columns[col] or diag1[row + col] or diag2[row - col]:
                    continue  # if columns/diag1/diag2 not safe, skip

                columns[col] = diag1[row + col] = diag2[row - col] = True
                count += backtrack(row + 1, columns, diag1, diag2)
                columns[col] = diag1[row + col] = diag2[row - col] = False
            return count

        return backtrack(0, columns, diag1, diag2)


def main():
    while True:
        try:
            line = input()
            n = stringToList(line)

            sol = Solution()
            ret = sol.totalNQueens(n)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
