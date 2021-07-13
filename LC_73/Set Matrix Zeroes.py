"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and 
column to 0's, and do it in place.
"""
from typing import List
from common_funcs import listToString, stringToList


class Solution:
    def setZeros(self, matrix: List[List[int]]) -> None:
        """
        Space Complexity: O(m + n), where m = len(matrix), n = len(matrix[0])
        """
        rows, cols = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    rows.add(i)
                    cols.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0

    def setZeros_2(self, matrix: List[List[int]]) -> None:
        """
        Whenever a 0 is encountered, set the first element of that column and 
        row to be 0; later revisit each cell to set them accordingly
        Time Complexity: O(1)
        """
        # whether the first column should be 0 or not, since matrix[0][0] is
        # used to represent the first row
        first_col = 1
        for i in range(len(matrix)):
            if not matrix[i][0]:
                first_col = 0
            for j in range(1, len(matrix[0])):
                if not matrix[i][j]:
                    matrix[i][0] = matrix[0][j] = 0

        # if the first cell is 0, set entire row/column 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if not matrix[0][0]:  # set first row accordingly
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if not first_col:  # set first column accordingly
            for i in range(len(matrix)):
                matrix[i][0] = 0


def main():
    while True:
        try:
            line = input()
            matrix = stringToList(line)
            matrix2 = stringToList(line)

            sol = Solution()
            sol.setZeros(matrix)
            sol.setZeros_2(matrix2)

            out = listToString(matrix)
            out2 = listToString(matrix2)
            print(f"Solved in O(m+n) space: {out}")
            print(f"Solved in O(1) space:   {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
