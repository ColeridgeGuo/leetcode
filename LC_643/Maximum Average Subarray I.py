"""
Given an array consisting of n integers, find the contiguous subarray of given
length k that has the maximum average value. And you need to output the maximum average value.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = res = sum(nums[:k])
        for i in range(len(nums)-k):
            res += nums[i+k] - nums[i]
            max_sum = max(max_sum, res)
        return max_sum / k


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.findMaxAverage(nums, k)
            
            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
