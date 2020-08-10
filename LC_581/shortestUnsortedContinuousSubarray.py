"""
Given an integer array, you need to find one continuous subarray that if you
only sort this subarray in ascending order, then the whole array will be sorted
in ascending order, too.
You need to find the shortest such subarray and output its length.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def findUnsortedSubarray_bubble(self, nums: List[int]) -> int:
        """
        Similar to bubble sort, keep track of l and r pointers whenever swapping
        occurs.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        l, r = len(nums), 0
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    l, r = min(l, j), max(r, j + 1)
        return 0 if r - l < 0 else r - l + 1

    def findUnsortedSubarray_selection(self, nums: List[int]) -> int:
        """
        Similar to selection sort, keep track of l and r pointers whenever
        swapping occurs.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        l, r = len(nums), 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    l, r = min(l, i), max(r, j)
        return 0 if r - l < 0 else r - l + 1

    def findUnsortedSubarray_sort(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n * log(n))
        Space Complexity: O(n)
        """
        snums = sorted(nums)
        l, r = len(nums), 0
        for i in range(len(nums)):
            if snums[i] != nums[i]:
                l, r = min(l, i), max(r, i)
        return 0 if r - l < 0 else r - l + 1
    
    def findUnsortedSubarray_stack(self, nums: List[int]) -> int:
        """
        Push ascending values onto a stack. Whenever a falling slope (out-of-
        order value) is seen, pop values off of the stack to determine its
        desired index. Do the same for reversely.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        l, r = len(nums), 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        stack.clear()
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        return 0 if r - l <= 0 else r - l + 1
    
    def findUnsortedSubarray_5(self, nums: List[int]) -> int:
        """
        Find the minimum and maximum values that are out of order first, then
        find the indices where they are supposed to be, take the difference
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        min_val, max_val = float('inf'), float('-inf')
        flag = False
        for i in range(1, len(nums)): # find minimum out-of-order value
            if nums[i] < nums[i - 1]:
                flag = True
            if flag:
                min_val = min(min_val, nums[i])
        flag = False
        for i in range(len(nums) - 2, -1, -1): # find maximum out-of-order value
            if nums[i] > nums[i + 1]:
                flag = True
            if flag:
                max_val = max(max_val, nums[i])
        l, r = 0, len(nums) - 1
        while l < len(nums):  # find min_val's desired index
            if min_val < nums[l]:
                break
            l += 1
        while r >= 0:  # find max_val's desired index
            if max_val > nums[r]:
                break
            r -= 1
        return 0 if r - l < 0 else r - l + 1


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            nums2 = stringToList(line)
            nums3 = stringToList(line)
            nums4 = stringToList(line)
            nums5 = stringToList(line)

            sol = Solution()
            ret_b = sol.findUnsortedSubarray_bubble(nums)
            ret_se = sol.findUnsortedSubarray_selection(nums2)
            ret_so = sol.findUnsortedSubarray_sort(nums3)
            ret_st = sol.findUnsortedSubarray_stack(nums4)
            ret_5 = sol.findUnsortedSubarray_5(nums5)
            out_b = str(ret_b)
            out_se = str(ret_se)
            out_so = str(ret_so)
            out_st = str(ret_st)
            out_5 = str(ret_5)
            
            print(f"Solved using bubble sort:     {out_b}")
            print(f"Solved using selection sort:  {out_se}")
            print(f"Solved by sorting:            {out_so}")
            print(f"Solved using a stack:         {out_st}")
            print(f"Solved w/o using extra space: {out_5}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
