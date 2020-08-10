"""
    You are a professional robber planning to rob houses along a street. Each
    house has a certain amount of money stashed, the only constraint stopping
    you from robbing each of them is that adjacent houses have security system
    connected and it will automatically contact the police if two adjacent
    houses were broken into on the same night.
    
    Given a list of non-negative integers representing the amount of money of
    each house, determine the maximum amount of money you can rob tonight
    without alerting the police.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def rob_DP(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        max_profit = [0]*len(nums)
        max_profit[0], max_profit[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            max_profit[i] = max(max_profit[i-1], max_profit[i-2] + nums[i])
        return max_profit[-1]


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret_DP = sol.rob_DP(nums)
            
            print(f"Solved with dynamic programming: {ret_DP}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
