"""
A robot is located at the top-left corner of a m x n grid. The robot can only 
move either down or right at any point in time. The robot is trying to reach the 
bottom-right corner of the grid.
Now consider if some obstacles are added to the grids. How many unique paths 
would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0]:  # return 0 immediately if start has an obstacle
            return 0
        grid[0][0] = 1  # otherwise start with 1

        # initialize first column
        # a cell has 1 path iff top cell is 1 and itself is not an obstacle
        for i in range(1, m):
            grid[i][0] = 0 if grid[i][0] else grid[i-1][0]

        # initialize first row
        # a cell has 1 path iff left cell is 1 and itself is not an obstacle
        for j in range(1, n):
            grid[0][j] = 0 if grid[0][j] else grid[0][j-1]

        # for each cell, # of paths if its left and top neighbors' paths,
        # or 0 if it's an obstacle
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = 0 if grid[i][j] else grid[i-1][j] + grid[i][j-1]
        return grid[-1][-1]

    def uniquePathsWithObstacles_2(self, grid: List[List[int]]) -> int:
        dp = [0] * len(grid[0])
        dp[0] = 1
        for row in grid:
            for j in range(len(row)):
                if row[j]:  # if obstacle
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[-1]


def main():
    while True:
        try:
            line = input()
            obstacleGrid = stringToList(line)
            obstacleGrid2 = stringToList(line)

            sol = Solution()
            ret = sol.uniquePathsWithObstacles(obstacleGrid)
            ret2 = sol.uniquePathsWithObstacles_2(obstacleGrid2)

            out = str(ret)
            out2 = str(ret2)
            print(f"Solved using dynamic programming 1: {out}")
            print(f"Solved using dynamic programming 2: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
