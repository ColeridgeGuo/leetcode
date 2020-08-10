"""
Given an unsorted array of integers, find the length of longest continuous
increasing subsequence (subarray).
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lcis, cis = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cis += 1
            else:
                lcis = max(lcis, cis)
                cis = 1
        return max(lcis, cis)
    
    def findLengthOfLCIS_sliding_window(self, nums: List[int]) -> int:
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i - 1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret = sol.findLengthOfLCIS(nums)
            ret_sw = sol.findLengthOfLCIS_sliding_window(nums)
            
            print(f"Solved by keeping tracking of CIS:   {ret}")
            print(f"Solved by marking boundaries of CIS: {ret_sw}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
