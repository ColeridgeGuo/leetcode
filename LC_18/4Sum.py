"""
Given an array nums of n integers and an integer target, are there elements a,
b, c, and d in nums such that a + b + c + d = target? Find all unique
quadruplets in the array which gives the sum of target.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lo, hi = j + 1, len(nums) - 1
                while lo < hi:
                    sum_ = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if sum_ < target:
                        lo += 1
                    elif sum_ > target:
                        hi -= 1
                    else:
                        res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        lo, hi = lo + 1, hi - 1
        return res
    
    def fourSum_nSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.nSum(nums, 4, target, 0)
    
    def nSum(self, nums: List[int], n: int, target: int, start: int) -> List[List[int]]:
        size = len(nums)
        res = []
        if n < 2 or size < n:
            return res
        if n == 2:  # solve 2Sum using two pointers
            lo, hi = start, size - 1
            while lo < hi:
                sum_ = nums[lo] + nums[hi]
                if sum_ < target:
                    lo += 1
                elif sum_ > target:
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo, hi = lo + 1, hi - 1
        else:  # when n > 2, recursively calculate (n-1)Sum
            i = start
            while i < size:
                sub = self.nSum(nums, n - 1, target - nums[i], i + 1)
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
                while i < size - 1 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
        return res


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            nums2 = stringToList(line)
            line = input()
            target = int(line)
            
            sol = Solution()
            ret = sol.fourSum(nums, target)
            ret_2 = sol.fourSum_nSum(nums2, target)
            
            out = listToString(ret)
            out_2 = listToString(ret_2)
            print(f"Solved directly by modifying 3Sum algo: {out}")
            print(f"Solved by calling nSum:                 {out_2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
