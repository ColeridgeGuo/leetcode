"""
Given a binary array nums and an integer k, return the maximum number of
consecutive 1's in the array if you can flip at most k 0's.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        To flip at most k 0's means that we have to find the longest subarray
        that contains at most k 0's.
        The left and right are boundaries of a sliding window which never
        shrinks; once it finds the max subarray so far, it will stay at least
        this long or grow longer if new max subarray is found.
        We move right boundary to include at most k 0's, then we need to move
        left boundary to find new windows that provide a longer subarray.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = right = 0  # initialize both boundaries
        for right in range(len(nums)):  # move right boundary
            if nums[right] == 0:
                k -= 1  # decrement k if we are including more 0's
            if k < 0:  # we have included more than k 0's
                if nums[left] == 0:
                    k += 1  # we are moving away from a 0, so increment k
                left += 1  # move left to the right to find new max subarray
        return right - left + 1


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.longestOnes(nums, k)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
