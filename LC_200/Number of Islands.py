"""
Given an m x n binary grid representing land and water, return the number of
islands formed by horizontally or vertically connected land cells.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(row: int, col: int) -> None:
            if row < 0 or row >= num_rows or col < 0 or col >= num_cols or grid[row][col] == '0':
                return
            grid[row][col] = '0'  # Mark the cell as visited
            dfs(row + 1, col)  # Down
            dfs(row - 1, col)  # Up
            dfs(row, col - 1) # Left
            dfs(row, col + 1) # Right

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        return num_islands

    def numIslands_bfs(self, grid :List[List[str]]) -> int:
        if not grid:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        num_islands = 0

        def bfs(row: int, col: int) -> None:
            from collections import deque
            queue = deque([(row, col)])
            grid[row][col] = '0'  # Mark the cell as visited

            while queue:
                i, j = queue.popleft()
                for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < num_rows and 0 <= y < num_cols and grid[x][y] == '1':
                        grid[x][y] = '0'  # Mark the cell as visited
                        queue.append((x, y))

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    bfs(i, j)
        return num_islands


def main():
    while True:
        try:
            line = input()
            grid = stringToList(line)
            grid2 = stringToList(line)

            sol = Solution()
            ret_dfs = sol.numIslands_dfs(grid)
            ret_bfs = sol.numIslands_bfs(grid2)

            out = str(ret_dfs)
            out2 = str(ret_bfs)
            print(f"Solved with DFS: {out}")
            print(f"Solved with BFS: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
