"""
    Given an array nums, write a function to move all 0's to the end of it while
    maintaining the relative order of the non-zero elements.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        - All elements before the slow pointer are non-zeroes.
        - All elements between the current and slow pointer are zeroes.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            sol.moveZeroes(nums)

            out = listToString(nums)

            print(f"Solved with two pointers: {out}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
