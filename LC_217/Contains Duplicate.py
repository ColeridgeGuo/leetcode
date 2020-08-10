"""
    Given an array of integers, find if the array contains any duplicates.
    Your function should return true if any value appears at least twice in the
    array, and it should return false if every element is distinct.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def containsDuplicate_pythonic(self, nums: List[int]) -> bool:
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        return len(set(nums)) < len(nums)
    
    def containsDuplicate_one_pass(self, nums: List[int]) -> bool:
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        nums_seen = set()
        for num in nums:
            if num in nums_seen:
                return True
            nums_seen.add(num)
        return False


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret_pythonic = sol.containsDuplicate_pythonic(nums)
            ret_one_pass = sol.containsDuplicate_one_pass(nums)
            
            print(f"Solved in a Pythonic way: {ret_pythonic}")
            print(f"Solved in one pass:       {ret_one_pass}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
