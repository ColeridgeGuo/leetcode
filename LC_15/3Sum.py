"""
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero
"""
from typing import List
from common_funcs import stringToList, stringToString_out


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return []


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret = sol.threeSum(nums)
            
            out = stringToString_out(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
