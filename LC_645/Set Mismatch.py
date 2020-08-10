"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the
data error, one of the numbers in the set got duplicated to another number in
the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error.
Your task is to firstly find the number occurs twice and then find the number
that is missing. Return them in the form of an array.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Time Complexity: O(4n) = O(n)
        Space Complexity: O(n)
        """
        nums_set = set(nums)
        nums_sum, nums_set_sum = sum(nums), sum(nums_set)
        duplicate = nums_sum - nums_set_sum
        missing = sum(range(1, len(nums)+1)) - nums_set_sum
        return [duplicate, missing]
    
    def findErrorNums_map(self, nums: List[int]) -> List[int]:
        """
        Time Complexity: O(2n) = O(n)
        Space Complexity: O(n)
        """
        from collections import Counter
        c = Counter(nums)
        duplicate, missing = 0, 0
        for i in range(1, len(nums)+1):
            if i in c:
                if c[i] == 2:
                    duplicate = i
            else:
                missing = i
        return [duplicate, missing]
    
    def findErrorNums_cnst_space(self, nums: List[int]) -> List[int]:
        """
        Time Complexity: O(2n) = O(n)
        Space Complexity: O(1)
        """
        duplicate = missing = 0
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1
        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1
                break
        return [duplicate, missing]
    
    def findErrorNums_xor(self, nums: List[int]) -> List[int]:
        """
        This method combines XOR and the constant-space method above. XORing all
        elements in nums with 1~n gives (duplicate ^ missing), then use the
        method above to find the duplicate and xor to find missing.
            (1 ^ 2 ^ ... ^ n) ^ (1 ^ 2 ^ ... ^ dup ^ dup ^ ... ^ n)
        =   (1 ^ 1) ^ (2 ^ 2) ^ ... ^ (dup ^ dup) ^ (miss ^ dup) ^ ... ^ (n ^ n)
        =   0 ^ 0 ^ ... ^ (miss ^ dup) ^ ... 0
        =   missing ^ duplicate
        
        Time Complexity: O(2n) = O(n)
        Space Complexity: O(1)
        """
        duplicate = missing = 0
        for i in range(len(nums)):
            val = abs(nums[i])
            missing ^= val ^ (i+1)
            if nums[val-1] < 0:
                duplicate = val
            else:
                nums[abs(val)-1] *= -1
        missing ^= duplicate
        return [duplicate, missing]


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            nums2 = stringToList(line)
            
            sol = Solution()
            ret = sol.findErrorNums(nums)
            ret_m = sol.findErrorNums_map(nums)
            ret_c = sol.findErrorNums_cnst_space(nums)
            ret_x = sol.findErrorNums_xor(nums2)
            
            print(f"Solved by converting to set: {ret}")
            print(f"Solved using Counter:        {ret_m}")
            print(f"Solved with constant space:  {ret_c}")
            print(f"Solved with XOR:             {ret_x}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
