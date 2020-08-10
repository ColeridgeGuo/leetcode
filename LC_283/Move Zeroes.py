"""
    Given an array nums, write a function to move all 0's to the end of it while
    maintaining the relative order of the non-zero elements.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def moveZeroes_del(self, nums: List[int]) -> None:
        """
            Time Complexity: O(n), if del is O(1)
            Space Complexity: O(k), where k = # of 0's
        """
        i = 0
        n = len(nums)
        num_zeros = 0
        while i < n:
            if nums[i] == 0:
                num_zeros += 1
                del nums[i]
                n -= 1
            else:
                i += 1
        for zero in range(num_zeros):
            nums.append(0)
        return
    
    def moveZeroes_swap(self, nums: list) -> None:
        """
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            # wait while we find a non-zero element to
            # switch with you
            if nums[slow] != 0:
                slow += 1
            # keep going
            fast += 1


def main():
    while True:
        try:
            line = input()
            nums1 = stringToList(line)
            nums2 = stringToList(line)
            
            sol = Solution()
            sol.moveZeroes_del(nums1)
            sol.moveZeroes_swap(nums2)
            
            print(nums1)
            print(nums2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
