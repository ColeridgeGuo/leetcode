"""
Given an array of integers nums sorted in ascending order, find the starting and
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        """
        def extreme_insertion_index(left):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                # either target < nums[mid], in which case we keep going left,
                # or target == nums[mid], in which case we only go left to find
                # the left end of the range if the boolean flag 'left' is true;
                # otherwise we go right
                if nums[mid] > target or (left and target == nums[mid]):
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        # find the left end of the range
        left_idx = extreme_insertion_index(True)

        # assert that left_idx is within the array bounds and that target is
        # actually found in nums
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        # return with the right end of the range
        return [left_idx, extreme_insertion_index(False) - 1]
    
    def searchRange_bisect(self, nums: List[int], target: int) -> List[int]:
        import bisect
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target) - 1
        return [left, right]

def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            target = int(line)
            
            sol = Solution()
            ret = sol.searchRange(nums, target)
            ret_b = sol.searchRange_bisect(nums, target)
            
            out = listToString(ret)
            out_b = listToString(ret_b)
            print(f"Solved using self-defined binary search function: {out}")
            print(f"Solved using Python's built-in bisect function:   {out_b}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
