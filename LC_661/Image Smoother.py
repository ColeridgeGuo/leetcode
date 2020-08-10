"""
Given a 2D integer matrix M representing the gray scale of an image, you need to
design a smoother to make the gray scale of each cell becomes the average gray
scale (rounding down) of all the 8 surrounding cells and itself. If a cell has
less than 8 surrounding cells, then use as many as you can.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        R, C = len(M), len(M[0])
        res = [[0] * C for _ in M]
        for i in range(R):
            for j in range(C):
                count = 0
                for nr in (i-1, i, i+1):
                    for nc in (j-1, j, j+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            res[i][j] += M[nr][nc]
                            count += 1
                res[i][j] //= count
        return res


def main():
    while True:
        try:
            line = input()
            image = stringToList(line)
            
            sol = Solution()
            ret = sol.imageSmoother(image)
            
            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
