"""
Given an unsorted integer array nums, find the smallest missing positive integer

Follow up: Could you implement an algorithm that runs in O(n) time and uses
constant extra space.?
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Put each number in its right place, e.g., 1,2,3,...,n. Then return the
        first index where its number is not right
        """
        n = len(nums)
        for i in range(n):
            # keep swapping the number at index i with the number at index
            # nums[i]-1 until it is at its correct position
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                swap = nums[i] - 1
                nums[i], nums[swap] = nums[swap], nums[i]
        # find the first index with incorrect number and return the index+1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1  # if all in order return length+1
    
    def firstMissingPositive_2(self, nums: List[int]) -> int:
        """
        After removing all the numbers greater than or equal to n, all the
        numbers remaining are smaller than n. If any number i appears, we add n
        to nums[i] which makes nums[i]>=n. Therefore, if nums[i]<n, it means i
        never appears in the array and we should return i.
        """
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(n):
            nums[nums[i] % n] += n
        for i in range(1, n):
            if nums[i] // n == 0:
                return i
        return n
    
    def firstMissingPositive_3(self, nums: List[int]) -> int:
        """
        Once all numbers are made positive, if any number x is found in range
        [1,N] then make the number at index x negative. Iterate through the list
        and return the index of the first positive number, meaning the number
        corresponding to its index did not appear in the original list
        """
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        for i in range(n):
            num = abs(nums[i])
            if num > n:
                continue
            num -= 1
            if nums[num] > 0:
                nums[num] *= -1
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        return n + 1

def main():
    while True:
        try:
            line = input()
            nums1 = stringToList(line)
            nums2 = stringToList(line)
            nums3 = stringToList(line)
            
            sol = Solution()
            ret = sol.firstMissingPositive(nums1)
            ret2 = sol.firstMissingPositive_2(nums2)
            ret3 = sol.firstMissingPositive_3(nums3)
            
            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            print(f'Solved by moving number to its correct location: {out}')
            print(f'Solved by adding length to each number:          {out2}')
            print(f'Solved by converting to negative:                {out3}')
        except StopIteration:
            break


if __name__ == '__main__':
    main()
