"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        rotate each number in the upper-left quadrant with its 3 counterparts
        """
        n = len(matrix)
        for i in range(n-n//2):
            for j in range(n//2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]

    def rotate_2(self, matrix: List[List[int]]) -> None:
        """
        reverse upside down and transpose pythonically
        """
        matrix[:] = zip(*matrix[::-1])

    def rotate_3(self, matrix: List[List[int]])-> None:
        """
        reverse upside down and transpose manually
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def main():
    while True:
        try:
            line = input()
            matrix = stringToList(line)
            matrix2 = stringToList(line)
            matrix3 = stringToList(line)

            sol = Solution()
            sol.rotate(matrix)
            sol.rotate_2(matrix2)
            sol.rotate_3(matrix3)

            out = listToString(matrix)
            out2 = listToString(matrix2)
            out3 = listToString(matrix3)
            print(out)
            print(out2)
            print(out3)
            # for row in matrix:
            #     for val in row:
            #         print(f'{val:3}', end="")
            #     print()

        except StopIteration:
            break


if __name__ == '__main__':
    main()
