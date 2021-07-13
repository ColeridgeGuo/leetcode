"""
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row > the last integer of the previous row.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Treat the 2D array as an 1D array and binary search for target
        Time Complexity: O(log(m * n)) or O(log(m) + log(n))
        """
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            row, col = divmod(mid, n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


def main():
    while True:
        try:
            line = input()
            matrix = stringToList(line)
            line = input()
            target = int(line)

            sol = Solution()
            ret = sol.searchMatrix(matrix, target)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
