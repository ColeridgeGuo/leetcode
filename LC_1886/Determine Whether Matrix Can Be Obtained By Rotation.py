"""
Given two n x n binary matrices mat and target, return true if it is possible to 
make mat equal to target by rotating mat in 90-degree increments, false otherwise.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def findRotation(self, mat: List[List[int]], 
                        target: List[List[int]]) -> bool:
        """
        Rotate the matrix 4 times to find valid rotation
        """
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(x) for x in zip(*mat[::-1])]
        return False
    
    def findRotation_2(self, mat: List[List[int]], 
                        target: List[List[int]]) -> bool:
        """
        Initialize an array of bools representing validity rotating 0/90/180/270 
        degrees. We then check each cell with its target in each rotation and 
        set to false if any one failed. Return if any rotation is valid.
        """
        c = [True] * 4
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j] != target[i][j]:
                    c[0] = False
                if mat[i][j] != target[~j][i]:
                    c[1] = False
                if mat[i][j] != target[~i][~j]:
                    c[2] = False
                if mat[i][j] != target[j][~i]:
                    c[3] = False
        return any(c)


def main():
    while True:
        try:
            line = input()
            mat = stringToList(line)
            line = input()
            target = stringToList(line)

            sol = Solution()
            ret = sol.findRotation(mat, target)
            ret2 = sol.findRotation_2(mat, target)

            out = str(ret)
            out2 = str(ret2)
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
