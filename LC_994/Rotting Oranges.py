"""
Given a grid of fresh and rotten oranges, return the minimum number of minutes
until no fresh oranges remain, or -1 if some fresh oranges cannot rot.
"""
from typing import List
from common_funcs import stringToList
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh += 1

        minutes = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            row, col, minute = queue.popleft()
            minutes = max(minutes, minute)

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # 入队时标记，避免重复入队
                    fresh -= 1
                    queue.append((nr, nc, minute + 1))

        return minutes if fresh == 0 else -1


def main():
    while True:
        try:
            line = input()
            grid = stringToList(line)

            sol = Solution()
            ret = sol.orangesRotting(grid)

            out = str(ret)
            print(out)
        except EOFError:
            break


if __name__ == '__main__':
    main()
