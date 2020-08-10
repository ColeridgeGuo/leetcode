"""
    Given an array of size n, find the majority element. The majority element is
    the element that appears more than ⌊ n/2 ⌋ times. You may assume that the
    array is non-empty and the majority element always exist in the array.
"""
from typing import List
from collections import Counter
from common_funcs import stringToList


class Solution:
    def majorityElement_counting(self, nums: List[int]) -> int:
        """
            Count the frequency of each number and return the majority one
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        count = Counter(nums)
        for num in set(nums):
            if count[num] > len(nums) / 2:
                return num

    def majorityElement_voting(self, nums: List[int]) -> int:
        """
            Boyer-Moore Majority Vote Algorithm
            http://www.cs.utexas.edu/~moore/best-ideas/mjrty/
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        major, counter = nums[0], 0
        for i in range(0, len(nums)):
            if not counter:
                major = nums[i]
                counter += 1
            else:
                counter = counter + 1 if nums[i] == major else counter - 1
        return major


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret_counting = sol.majorityElement_counting(nums)
            ret_voting = sol.majorityElement_voting(nums)
            
            print(f"Solved with counting:     {ret_counting}")
            print(f"Solved with Moore voting: {ret_voting}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
