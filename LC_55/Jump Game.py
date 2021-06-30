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
        max_reach = 0  # farthest index we can reach so far, initially 0
        for i in range(len(nums)):
            # return true if we can reach or exceed the last index
            if max_reach >= len(nums) - 1:
                return True
            # update max_reach with current jump + current index
            max_reach = max(max_reach, i + nums[i])
            # return false if we are stuck here (nums[i] = 0)
            if max_reach == i:
                return False
        
    def canJump_2(self, nums: List[int]) -> bool:
        last = len(nums) - 1  # assume that we have reached the last index
        for i in range(len(nums) - 2, -1, -1):  # from back to front
            # if last can be reached from current index, update last index
            if nums[i] + i >= last:
                last = i
        return last == 0  # check if we can go back to the beginning


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.canJump(nums)
            ret2 = sol.canJump_2(nums)

            out = str(ret)
            out2 = str(ret2)
            print(f"Solved from front to back: {out}")
            print(f"Solved from back to front: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
