"""
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero
"""
from typing import List
from common_funcs import stringToList, stringToString_out


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            tuples = self.twoSum(nums, i + 1, -nums[i])
            for tup in tuples:
                tup.append(nums[i])
                res.append(tup)
            
        return res
    
    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        lo, hi = start, len(nums) - 1
        res = []
        while lo < hi:
            sum_ = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if sum_ < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif sum_ > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res
    
    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum_ = nums[i] + nums[lo] + nums[hi]
                if sum_ < 0:
                    lo += 1
                elif sum_ > 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo, hi = lo + 1, hi - 1
        return res


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            nums2 = stringToList(line)
            
            sol = Solution()
            ret = sol.threeSum(nums)
            ret_2 = sol.threeSum_2(nums2)
            
            out = stringToString_out(ret)
            out_2 = stringToString_out(ret_2)
            print(f"Solved with a separate TwoSum:  {out}")
            print(f"Solved by incorporating TwoSum: {out_2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
