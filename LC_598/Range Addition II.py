"""
Given an m * n matrix M initialized with all 0's and several update operations.
Operations are represented by a 2D array, and each operation is represented by
an array with two positive integers a and b, which means M[i][j] should be added
by one for all 0 <= i < a and 0 <= j < b.
You need to count and return the number of maximum integers in the matrix after
performing all the operations.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """
        Time complexity : O(x), x refers to the number of operations.
        Space complexity : O(1)
        """
        max_i, max_j = m, n
        for op in ops:
            max_i, max_j = min(max_i, op[0]), min(max_j, op[1])
        return max_i * max_j


def main():
    while True:
        try:
            line = input()
            m = int(line)
            line = input()
            n = int(line)
            line = input()
            ops = stringToList(line)
            
            sol = Solution()
            ret = sol.maxCount(m, n, ops)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
