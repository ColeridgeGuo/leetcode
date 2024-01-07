"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the
left of the index is equal to the sum of all the numbers strictly to the index's
right.

If the index is on the left edge of the array, then the left sum is 0 because
there are no elements to the left. This also applies to the right edge of the
array.

Return the leftmost pivot index. If no such index exists, return -1.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i, n in enumerate(nums):
            right -= n
            if left == right:
                return i
            left += n
        return -1


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.pivotIndex(nums)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
