"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def singleNumber_dictonary(self, nums: List[int]) -> int:
        """
            Time complexity: O(1*n) = O(n)
            Space complexity: O(n)
        """
        from collections import defaultdict
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for num in dic:
            if dic[num] == 1:
                return num
            
    def singleNumber_math(self, nums: List[int]) -> int:
        """
            Time complexity: O(n+n) = O(n)
            Space complexity: O(n+n) = O(n)
        """
        return sum(set(nums))*2 - sum(nums)
    
    def singleNumber_bit(self, nums: List[int]) -> int:
        """
            any bit XOR 0 = same bit
            any bit XOR 1 = inverse bit
            Time complexity: O(n)
            Space complexity: O(1)
        """
        bit = 0
        for num in nums:
            bit ^= num
        return bit


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret_dictionary = sol.singleNumber_dictonary(nums)
            ret_math = sol.singleNumber_math(nums)
            ret_bit = sol.singleNumber_bit(nums)
            
            print(f"Solved with dictionary:       {ret_dictionary}")
            print(f"Solved with math:             {ret_math}")
            print(f"Solved with bit manipulation: {ret_bit}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
