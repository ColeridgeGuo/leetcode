"""
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
    find the one that is missing from the array.
    
    Your algorithm should run in linear runtime complexity.
    Could you implement it using only constant extra space complexity?
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
            Time Complexity: O(n)
            Space Complexity: (1)
        """
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
    
    def missingNumber_bit(self, nums: List[int]) -> int:
        """
            Time Complexity: O(n)
            Space Complexity: (1)
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret = sol.missingNumber(nums)
            ret_bit = sol.missingNumber_bit(nums)
            
            print(f"Solved using Gauss' Formula to calculate sum: {ret}")
            print(f"Solved using bit manipulation:                {ret_bit}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
