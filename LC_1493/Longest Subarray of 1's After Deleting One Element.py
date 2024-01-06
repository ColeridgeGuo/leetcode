"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the
resulting array. Return 0 if there is no such subarray.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Reused the same algorithm from #1004, except that we have at most one 0
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = right = 0  # initialize both boundaries
        k = 1  # the max number of 0's we can have
        for right in range(len(nums)):  # move right boundary
            if nums[right] == 0:
                k -= 1  # decrement k if we are including more 0's
            if k < 0:  # we have included more than k 0's
                if nums[left] == 0:
                    k += 1  # we are moving away from a 0, so increment k
                left += 1  # move left to the right to find new max subarray
        return right - left

    def longestSubarray_2(self, nums: List[int]) -> int:
        """
        Use a sliding window to find the max subarray with at most one 0.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        ans = k = left = 0
        for right in range(len(nums)):
            k += nums[right] == 0  # increment k if we include more 0
            while k > 1:  # we have included more than one 0
                k -= nums[left] == 0  # decrement k if we are excluding a 0
                left += 1  # move left to the right to new max subarray
            ans = max(ans, right - left)
        return ans


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.longestSubarray(nums)
            ret2 = sol.longestSubarray_2(nums)

            print(f"Solved with non-shrinking sliding window: {ret}")
            print(f"Solved with shrinking sliding window:     {ret2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
