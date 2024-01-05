"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k
and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""
import collections
from typing import List
from common_funcs import stringToList


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        For each number x, we need to pair it with k - x to remove the pair.
        The max operation depends on the minimum frequency of x and k - x, so we
        can pair at most min(freq[x], freq[k-x]) times.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        freq = collections.Counter(nums)
        ans = 0
        for num in freq:
            ans += min(freq[k - num], freq[num])
        return ans // 2

    def maxOperations_sort(self, nums: List[int], k: int) -> int:
        """
        Sort nums first. Start from two ends and move either/both pointers
        inward until we have a pair that sum up to k.

        Time Complexity: O(n*log(n))
        Space Complexity: O(1)
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = 0
        while left < right:
            if nums[left] + nums[right] == k:
                ans += 1
                left, right = left + 1, right - 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return ans


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            nums2 = stringToList(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.maxOperations(nums, k)
            ret2 = sol.maxOperations_sort(nums2, k)

            print(f"Solved by counting frequencies:           {ret}")
            print(f"Solved by sorting and using two pointers: {ret2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
