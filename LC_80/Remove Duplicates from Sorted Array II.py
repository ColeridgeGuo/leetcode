"""
Given an integer array nums sorted in non-decreasing order, remove some 
duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you 
must instead have the result be placed in the first part of the array nums. More 
formally, if there are k elements after removing the duplicates, then the first 
k elements of nums should hold the final result. It does not matter what you 
leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the 
input array in-place with O(1) extra memory.
"""
from typing import List
from common_funcs import listToString, stringToList


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Pointer i is always before or equal to pointer n.

        If n <= i-2, we know that n must equal i-2 because nums is non-decresing
        Therefore all of i-2, i-1, i/n are the same and we have more than 2 
        duplicates. In this case i stay out to be replaced by next different num

        Otherwise i is replaced by a new num that is different from i-2 to 
        ensure duplicates appear no more than twice
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.removeDuplicates(nums)

            out = listToString(nums[:ret])
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
