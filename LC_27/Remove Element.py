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
        When nums[j] == val, skip this element by incrementing j. As long as 
        nums[j] != val, we copy nums[j] to nums[i] and increment both indexes at 
        the same time. Repeat the process until j reaches the end of the array 
        and the new length is i.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

    def removeElement_2(self, nums: List[int], val: int) -> int:
        """
        When elements to remove are rare, we swap elements that equal to val 
        with the last element and decrease array length by 1 to avoid 
        unnecessary swaps
        """
        i, n = 0, len(nums)
        while i < n:
            if (nums[i] == val):
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

            print(f"Solved by swapping non-val elements: {nums1[:ret]}")
            print(f"Solved by swapping non-val elements: {nums2[:ret2]}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
