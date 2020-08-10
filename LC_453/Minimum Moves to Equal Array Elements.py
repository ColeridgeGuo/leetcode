"""
    Given a non-empty integer array of size n, find the minimum number of moves
    required to make all array elements equal, where a move is incrementing
    n - 1 elements by 1.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
            Let N = len(nums), MIN = min(nums), SUM = sum(nums)
            If after M moves, we get all the numbers as X, then
                SUM + M * (N - 1) = X * N
            However, MIN will always be min until it reaches the X, because
            every move, other numbers (besides the max) will be incremented too.
            Therefore, X = MIN + M,
                SUM + M * N - M = (MIN + M) * N
                SUM + M * N - M = MIN * N + M * N
                SUM - M = MIN * N
                M = SUM - MIN * N
            
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        return sum(nums) - min(nums)*len(nums)


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.minMoves(nums)
            
            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
