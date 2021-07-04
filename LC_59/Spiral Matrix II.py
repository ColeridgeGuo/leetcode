"""
Given a positive integer n, generate an n x n matrix filled with elements from 
1 to n^2 in spiral order.
"""
from typing import List
from common_funcs import listToString


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(res), lo
            # add new top row to rotated bottom portion
            res = [[*range(lo, hi)]] + [list(x) for x in zip(*reversed(res))]
        return res

    def generateMatrix_2(self, n: int) -> List[List[int]]:
        """
        Walk spirally in the nxn matrix and filling up numbers from 1 to n, with 
        i,j representing current coordinates and di,dj directions to go.
        """
        res = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1  # initially we go right so di=0 and dj=1
        for k in range(n*n):
            res[i][j] = k + 1  # fill up matrix
            if res[(i+di) % n][(j+dj) % n]:
                di, dj = dj, -di  # change direction if we reach boundaries
            i += di  # walk in the current direction
            j += dj
        return res

    def generateMatrix_3(self, n: int) -> List[List[int]]:
        """
        Walk spirally in the nxn matrix and filling up numbers from 1 to n, 
        keeping tracking of 4 current boundaries and avoid going out of bounds
        """
        res = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        num = 1
        while top <= bottom and left <= right:
            # traverse right
            for j in range(left, right+1):
                res[top][j] = num
                num += 1
            top += 1
            # traverse down
            for i in range(top, bottom+1):
                res[i][right] = num
                num += 1
            right -= 1
            # traverse left
            for j in range(right, left-1, -1):
                if top <= bottom:
                    res[bottom][j] = num
                num += 1
            bottom -= 1
            # traverse up
            for i in range(bottom, top-1, -1):
                if left <= right:
                    res[i][left] = num
                num += 1
            left += 1
        return res


def main():
    while True:
        try:
            line = input()
            n = int(line)

            sol = Solution()
            ret = sol.generateMatrix(n)
            ret2 = sol.generateMatrix_2(n)
            ret3 = sol.generateMatrix_3(n)

            out = listToString(ret)
            out2 = listToString(ret2)
            out3 = listToString(ret3)
            print(f"Solved by rotating and adding new row on top: {out}")
            print(f"Solved by spirally filling out the numbers:   {out2}")
            print(f"Solved by simulating spiral matrix:           {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
