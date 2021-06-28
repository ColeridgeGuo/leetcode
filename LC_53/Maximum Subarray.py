"""
Given an integer array nums, find the contiguous subarray (containing at least 
one number) which has the largest sum and return its sum.
"""
from typing import List, Tuple
from common_funcs import stringToList


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        A refined concise version of the next one
        Time Complexity: O(n)
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

    def maxSubArray_2(self, nums: List[int]) -> int:
        """
        dp[i]: the max sum of nums[0:i]
        dp[i] = dp[i-1] + nums[i] if dp[i-1] > 0
                    0   + nums[i] if dp[i-1] <= 0
        If nums[0:i] subarray does not provide a positive value to make the max 
        sum greater, then we ignore it altogether; otherwise we include it.
        Time Complexity: O(n)
        """
        dp = [nums[0]] * len(nums)
        max_ = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            max_ = max(max_, dp[i])
        return max_

    def maxSubArray_dc(self, nums: List[int]) -> int:
        """
        Recursive Divide-and-Conquer algorithm: keep spliting nums into halves 
        and find the max subarray sum in each half. The max sum subarray either 
        lies entirely in the left/right half, or lies across two halves. We keep 
        track of the max sum starting at the first element and ending at the 
        last element so that max sum across two halves can be determined.
        """

        def divide_n_conquer(lo: int, hi: int) -> Tuple[int, int, int, int]:
            """
            The returned tuple's 4 elements represent:\n
            0. max subarray sum in nums[i:j] including nums[i]
            1. max subarray sum in nums[i:j] anywhere
            2. max subarray sum in nums[i:j] including nums[j]
            3. sum of all values in nums[i:j]
            """
            if lo == hi - 1:
                return [nums[lo]] * 4
            mid = (lo + hi) // 2
            left = divide_n_conquer(lo, mid)
            right = divide_n_conquer(mid, hi)
            max_sum_i = max(left[0], left[3] + right[0])
            max_sum_j = max(right[2], right[3] + left[2])
            max_sum_ = max(left[1], right[1], left[2] + right[0])
            sum_ = left[3] + right[3]
            return max_sum_i, max_sum_, max_sum_j, sum_

        return divide_n_conquer(0, len(nums))[1]


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            nums2 = stringToList(line)

            sol = Solution()
            ret = sol.maxSubArray(nums)
            ret2 = sol.maxSubArray_dc(nums2)

            out = str(ret)
            out2 = str(ret2)
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
