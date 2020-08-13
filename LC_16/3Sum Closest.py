"""
Given an array nums of n integers and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        nums.sort()
        # max number target could be, max difference between sum and target
        res, diff = 0, float('inf')
        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                three_sum = nums[i] + nums[lo] + nums[hi]
                
                # if a new min 3sum occurs, update res and diff
                if abs(target - three_sum) < diff:
                    res, diff = three_sum, abs(target - three_sum)
                # 3sum < target means we need greater numbers to be closer
                if three_sum < target:
                    lo += 1
                # 3sum > target means we need smaller numbers to be closer
                elif three_sum > target:
                    hi -= 1
                # if 3sum == target then immediately return
                else:
                    return res
        return res
    
    def threesumClosest_bisect(self, nums: List[int], target: int) -> int:
        """
        Time Complexity: O(n^2 * log(n))
        Space Complexity: O(n)
        """
        from bisect import bisect
        diff = float('inf')  # max difference between sum and target
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                comp = target - nums[i] - nums[j]  # fix two numbers
                # binary search to find the third number
                hi = bisect(nums, comp, lo=j + 1)
                lo = hi - 1
                if hi < len(nums) and abs(comp - nums[hi]) < abs(diff):
                    diff = comp - nums[hi]
                if lo > j and abs(comp - nums[lo]) < abs(diff):
                    diff = comp - nums[lo]
            if diff == 0:
                break
        return target - diff


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            nums2 = stringToList(line)
            line = input()
            target = int(line)
            
            sol = Solution()
            ret = sol.threeSumClosest(nums, target)
            ret_b = sol.threesumClosest_bisect(nums2, target)
            
            print(f"Solved using two pointers:  {ret}")
            print(f"Solved using binary search: {ret_b}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
