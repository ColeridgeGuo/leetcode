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
        Then we greedily find the next greatest jump with in [l, r] we can make, 
        and adjust [l,r] accordingly until we reach the end
        """
        l, r, jumps = 0, 0, 0
        while r < len(nums) - 1:
            jumps += 1
            l, r = r + 1, max(i + nums[i] for i in range(l, r+1))
        return jumps


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.jump(nums)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
