"""
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def twoSum_hashmap(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        comps = {}
        for i, num in enumerate(nums):
            comp = target - num
            if num in comps:
                return [comps[num], i]
            comps[comp] = i
            
    def twoSum_2pointers(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n * log(n))
        Space Complexity: O(1) if snums ignored
        """
        snums = enumerate(nums)
        snums = sorted(snums, key=lambda x:x[1])
        lo, hi = 0, len(snums) - 1
        while lo < hi:
            sum_ = snums[lo][1] + snums[hi][1]
            if sum_ < target:
                lo += 1
            elif sum_ > target:
                hi -= 1
            else:
                return sorted([snums[lo][0], snums[hi][0]])


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            target = int(line)
            
            sol = Solution()
            ret_h = sol.twoSum_hashmap(nums, target)
            ret_t = sol.twoSum_2pointers(nums, target)
            
            out_h = listToString(ret_h)
            out_t = listToString(ret_t)
            print(f"Solved using hashmap:      {out_h}")
            print(f"Solved using two pointers: {out_t}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
