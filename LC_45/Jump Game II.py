"""
Given an array of non-negative integers nums, you are initially positioned at 
the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Starting from l, the farthest I can go in one jump is r. 
        Then we greedily find the next greatest jump within [l, r] we can make,
        and adjust [l,r] accordingly until we reach the end.
        """
        l, r, jumps = 0, 0, 0
        while r < len(nums) - 1:
            jumps += 1
            l, r = r + 1, max(i + nums[i] for i in range(l, r+1))
        return jumps

    def jump_2(self, nums: List[int]) -> int:
        """
        Greedily find the farthest jump we can make from each position.
        Update the right boundary when we reach the current boundary.
        Increment jumps when we cross the current boundary.
        """
        jumps = right_boundary = max_reach = 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == right_boundary:
                jumps += 1
                right_boundary = max_reach
        return jumps


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.jump(nums)
            ret2 = sol.jump_2(nums)

            out = str(ret)
            out2 = str(ret2)
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
