"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            # traverse right
            for j in range(left, right+1):
                res.append(matrix[top][j])
            top += 1

            # traverse down
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            # traverse left
            if top > bottom:
                break
            for j in range(right, left-1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1

            # traverse up
            if left > right:
                break
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
    
    def spiralOrder_2(self, matrix: List[List[int]]) -> List[int]:
        return matrix and \
            [*matrix.pop(0)] + self.spiralOrder_2([*zip(*matrix)][::-1])

def main():
    while True:
        try:
            line = input()
            matrix = stringToList(line)
            matrix2 = stringToList(line)

            sol = Solution()
            ret = sol.spiralOrder(matrix)
            ret2 = sol.spiralOrder_2(matrix2)

            out = listToString(ret)
            out2 = listToString(ret2)
            print(f"Solved by directly simulating spiral order:  {out}")
            print(f"Solved by rotating and taking the first row: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
