"""
Given an array of non-negative integers nums, you are initially positioned at 
the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # farthest index we can reach so far
        for i in range(len(nums)):  # visit every index in order
            if i > max_reach:  # current index is unreachable
                return False
            max_reach = max(max_reach, i + nums[i])  # extend reach from index i
        return True  # every index was reachable, so the last index is reachable

    def canJump_2(self, nums: List[int]) -> bool:
        reach = len(nums) - 1  # leftmost index currently known to reach the end
        for i in range(len(nums) - 2, -1, -1):  # check each earlier index
            if nums[i] + i >= reach:  # index i can jump to the current goal
                reach = i  # index i becomes the new goal
        return reach == 0  # start index can reach the end only if goal moved to 0

    def canJump_3(self, nums: List[int]) -> bool:
        gas = 0  # steps we can still move before getting stuck
        for n in nums:
            if gas < 0:  # no gas means this position cannot be reached
                return False
            elif n > gas:  # current position gives us more reach than we had
                gas = n  # refill gas to this position's jump length
            gas -= 1  # spend one step moving to the next index
        return True  # made it through the array without getting stranded


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.canJump(nums)
            ret2 = sol.canJump_2(nums)
            ret3 = sol.canJump_3(nums)

            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            print(f"Solved from front to back: {out}")
            print(f"Solved from back to front: {out2}")
            print(f"Solved with gas tank:      {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
