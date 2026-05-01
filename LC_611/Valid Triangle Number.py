"""
Given an integer array nums, return the number of triplets chosen from the array
that can make triangles if we take them as side lengths of a triangle.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Sort the array so that for any fixed longest side nums[c], we can use two
        pointers a and b to find valid shorter sides. When nums[a] + nums[b] >
        nums[c], every value between a and b can pair with nums[b] and nums[c]
        to form a triangle because the array is sorted, so we can count b - a
        triplets at once. Otherwise, we move a right to increase the sum.

        Time Complexity: O(n^2)
        Space Complexity: O(1) excluding the sort implementation
        """
        nums.sort()

        res = 0
        # Use a, b, c as three sides of a triangle, c being the longest
        for c in range(len(nums) - 1, 1, -1):
            a, b = 0, c - 1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    res += b - a
                    b -= 1
                else:
                    a += 1

        return res


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.triangleNumber(nums)

            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
