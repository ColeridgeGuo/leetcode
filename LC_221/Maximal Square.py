"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square 
containing only 1's and return its area.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        dp[i][j]: side length of the maximum square with bottom-right corner at 
                    (i,j)
        - if a cell itself is 0, then no square can be formed here
        - otherwise the max side length is the minimum of its top-left three 
        neighbors + 1 because a larger square can only be formed by expanding a 
        smaller square diagonally to the bottom-right

        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        max_sq_len = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    max_sq_len = max(max_sq_len, dp[i][j])
        return max_sq_len * max_sq_len

    def maximalSquare_2(self, matrix: List[List[str]]) -> int:
        """
        Optimize space by using 1-D array to store only the previous row's info.
            dp[i-1]: dp value for left neighbor
            dp[i]  : dp value for top neighbor, to be updated
            prev   : dp value for top-left neighbor
        Time Complexity: O(m*n)
        Space Complexity: O(n)
        """
        m, n = len(matrix), len(matrix[0])
        dp = [0]*(n+1)
        max_sq_len = 0
        prev = 0
        for i in range(m):
            for j in range(n):
                temp = dp[j]
                if matrix[i][j] == '1':
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    max_sq_len = max(max_sq_len, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return max_sq_len * max_sq_len


def main():
    while True:
        try:
            line = input()
            matrix = stringToList(line)

            sol = Solution()
            ret = sol.maximalSquare(matrix)
            ret2 = sol.maximalSquare_2(matrix)

            out = str(ret)
            out2 = str(ret2)
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
