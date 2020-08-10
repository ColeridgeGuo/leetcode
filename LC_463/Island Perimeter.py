"""
    You are given a map in form of a two-dimensional integer grid where 1
    represents land and 0 represents water. Grid cells are connected
    horizontally/vertically (not diagonally). The grid is completely surrounded
    by water, and there is exactly one island (i.e., one or more connected land
    cells). The island doesn't have "lakes" (water inside that isn't connected
    to the water around the island). One cell is a square with side length 1.
    The grid is rectangular, width and height don't exceed 100.
    Determine the perimeter of the island.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        islands = neighbors = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    islands += 1
                    if i < len(grid) - 1 and grid[i+1][j]:
                        neighbors += 1
                    if j < len(grid[i]) - 1 and grid[i][j+1]:
                        neighbors += 1
        return 4 * islands - 2 * neighbors


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret = sol.islandPerimeter(nums)
            
            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
