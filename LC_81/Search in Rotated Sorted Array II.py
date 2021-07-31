"""
There is an integer array nums sorted in non-decreasing order (not necessarily 
with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index 
k (0 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]. 
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become 
[4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if 
target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return True
            # if nums[mid] == nums[lo], both sides are ordered so we skip all
            # the same nums
            while lo < mid and nums[lo] == nums[mid]:
                lo += 1
            if nums[lo] <= nums[mid]:  # left side is ordered
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1  # target is in the left side so search left
                else:
                    lo = mid + 1  # otherwise search right
            else:  # right side is ordered
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1  # target is in the right side so search right
                else:
                    hi = mid - 1  # otherwise search left
        return False


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            target = int(line)

            sol = Solution()
            ret = sol.search(nums, target)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
