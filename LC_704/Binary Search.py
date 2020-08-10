"""
Given a sorted (in ascending order) integer array nums of n elements and a
target value, write a function to search target in nums. If target exists, then
return its index, otherwise return -1.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def search_bisect(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        index = bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            target = int(line)
            
            sol = Solution()
            ret_bi = sol.search_bisect(nums, target)
            ret = sol.search(nums, target)
            
            print(f"Solved using Python's bisect library: {ret_bi}")
            print(f"Solved with binary search:            {ret}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
