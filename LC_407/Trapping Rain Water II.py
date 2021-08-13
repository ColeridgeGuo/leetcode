"""
Given an m x n integer matrix heightMap representing the height of each unit 
cell in a 2D elevation map, return the volume of water it can trap after raining
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        Start from the lowest bars on the borders of the heightMap and work our 
        way inward, follow the so-far unvisited lowest bar from which the water 
        would leak if any. Any bar lower than the current lowest bar would trap 
        water equal to their difference
        Time Complexity: 
        Space Complexity: 
        """
        import heapq
        water = 0
        m, n = len(heightMap), len(heightMap[0])
        heap = []

        # push all border cells onto the min heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

        # start with the lowest cell and BFS its neighbors for a lower cell
        level = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            level = max(height, level)
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and heightMap[x][y] != -1:
                    heapq.heappush(heap, (heightMap[x][y], x, y))
                    water += max(0, level - heightMap[x][y])
                    heightMap[x][y] = -1
        return water


def main():
    while True:
        try:
            line = input()
            heightMap = stringToList(line)

            sol = Solution()
            ret = sol.trapRainWater(heightMap)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
