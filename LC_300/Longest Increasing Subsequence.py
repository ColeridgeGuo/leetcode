"""
Given an integer array nums, return the length of the longest strictly
increasing subsequence.
"""
from typing import List
from bisect import bisect_left

from common_funcs import stringToList


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Store the longest increasing subsequence ending at each index by
        comparing that value with every earlier smaller value.
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


    def lengthOfLIS_2(self, nums: List[int]) -> int:
        """
        Maintain the smallest possible tail for each subsequence length;
        bisect_left replaces tails without changing the current lengths.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        tails = []

        for number in nums:
            position = bisect_left(tails, number)

            if position == len(tails):
                tails.append(number)
            else:
                tails[position] = number

        return len(tails)


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.lengthOfLIS(nums)
            ret2 = sol.lengthOfLIS_2(nums)

            out = str(ret)
            out2 = str(ret2)
            print(f"Solved with dynamic programming: {out}")
            print(f"Solved with binary search:       {out2}")
        except EOFError:
            break


if __name__ == '__main__':
    main()
