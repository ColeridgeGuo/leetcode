"""
Given a m x n grid filled with non-negative numbers, find a path from top left 
to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not i and not j:  # do nothing at (0,0)
                    continue
                elif not i:  # simply add left neighbor for first row
                    grid[i][j] += grid[i][j-1]
                elif not j:  # simply add top neighbor for first column
                    grid[i][j] += grid[i-1][j]
                else:  # pick min between left and top neighbors for all others
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]


def main():
    while True:
        try:
            line = input()
            grid = stringToList(line)

            sol = Solution()
            ret = sol.minPathSum(grid)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
