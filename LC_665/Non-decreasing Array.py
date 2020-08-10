"""
Given an array nums with n integers, your task is to check if it could become
non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i
(0-based) such that (0 <= i <= n - 2).
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        Let p be the unique problem index for which nums[p] > nums[p+1]. If this
        is not unique, return False; or if it doesn't exist, return True.
        We analyze the following cases:
        - If p = 0,
            then we could make the array good by setting nums[p] = nums[p+1].
        - If p = len(nums) - 2,
            then we could make the array good by setting nums[p+1] = nums[p].
        - Otherwise, nums[p-1], nums[p], nums[p+1], nums[p+2] all exist, and:
            - change nums[p] to between nums[p-1] and nums[p+1] if possible, or;
            - change nums[p+1] to between nums[p] and nums[p+2] if possible.
        """
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:  # if p is not unique
                    return False
                p = i  # the index where out-of-order occurs
        return not p or p == len(nums)-2 or \
            nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2]


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret = sol.checkPossibility(nums)

            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
