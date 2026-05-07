"""
Given an integer array nums and an integer val, remove all occurrences of val in 
nums in-place. The relative order of the elements may be changed.
Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the 
input array in-place with O(1) extra memory.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Similar to leetcode 283 - Move Zeroes, we use slow and fast pointers to
        move non-val elements to the front of the array. The slow pointer only
        moves when we find a non-val element, while the fast pointer looks ahead
        for non-val elements.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast] # not swapping here as we don't care
                slow += 1
        return slow

    def removeElement_2(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1  # reduce array size by one
            else:
                i += 1
        return n


def main():
    while True:
        try:
            line = input()
            nums1 = stringToList(line)
            nums2 = stringToList(line)
            line = input()
            val = int(line)

            sol = Solution()
            ret = sol.removeElement(nums1, val)
            ret2 = sol.removeElement_2(nums2, val)

            print(f"Solved with slow/fast pointers: {nums1[:ret]}")
            print(f"Solved with two pointers:       {nums2[:ret2]}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
