"""
Given an integer array nums sorted in non-decreasing order, remove the 
duplicates in-place such that each unique element appears only once. The 
relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you 
must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the 
first k elements of nums should hold the final result. It does not matter 
what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the 
input array in-place with O(1) extra memory.
"""
from typing import List
from common_funcs import listToString, stringToList


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Use 2 pointers, one to loop thru the array, one to mark where the new 
        array ends. We skip all the same nums as new_end, and swap different 
        number with new_end, thus removing duplicates.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
        new_end = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[new_end]:
                new_end += 1
                nums[new_end] = nums[i]
        return new_end + 1

    def removeDuplicates_2(self, nums: List[int]) -> int:
        """
        Count the number of duplicates and swap different number w/ the index 
        where it would go if there were no duplicates
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                nums[i - count] = nums[i]
        return len(nums) - count


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            nums2 = stringToList(line)

            sol = Solution()
            ret = sol.removeDuplicates(nums)
            ret2 = sol.removeDuplicates_2(nums2)

            out = listToString(nums[:ret])
            out2 = listToString(nums2[:ret2])
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
