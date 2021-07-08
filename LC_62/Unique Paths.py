"""
A robot is located at the top-left corner of a m x n grid. The robot can only 
move either down or right at any point in time. The robot is trying to reach the 
bottom-right corner of the grid.
How many possible unique paths are there?
"""


class Solution:
    def uniquePaths_dp(self, m: int, n: int) -> int:
        """
        We can only reach (i, j) through (i-1, j) and (i, j-1), so we can just 
        add up the number of paths to reach those two points.
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    def uniquePaths_dp2(self, m: int, n: int) -> int:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(n)
        """
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]

    def uniquePaths_math(self, m: int, n: int) -> int:
        """
        We need m-1 steps down and n-1 steps right to reach the end, so a total 
        of m+n-2 steps. Use formula to calculate (m+n-2) choose (m-1) or (n-1)
        """
        from math import factorial
        return factorial(m+n-2) // factorial(n-1) // factorial(m-1)


def main():
    while True:
        try:
            line = input()
            m = int(line)
            line = input()
            n = int(line)

            sol = Solution()
            ret = sol.uniquePaths_dp(m, n)
            ret2 = sol.uniquePaths_dp2(m, n)
            ret3 = sol.uniquePaths_math(m, n)

            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            print(f"Solved using dynamic programming:   {out}")
            print(f"Solved using dynamic programming 2: {out2}")
            print(f"Solved using math:                  {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
