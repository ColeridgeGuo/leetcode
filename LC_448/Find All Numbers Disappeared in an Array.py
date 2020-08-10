"""
    Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
    elements appear twice and others appear once.
    Find all the elements of [1, n] inclusive that do not appear in this array.
    Could you do it without extra space and in O(n) runtime? You may assume the
    returned list does not count as extra space.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        return list(set(range(1, len(nums) + 1)) - set(nums))
    
    def findDisappearedNumbers_2(self, nums: List[int]) -> List[int]:
        """
            For each number i in nums, we mark the number that i points as
            negative. Then we filter the list, get all the indexes who points to
            a positive number.
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        for num in nums:
            index = abs(num) - 1
            nums[index] = - abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.findDisappearedNumbers(nums)
            ret_2 = sol.findDisappearedNumbers_2(nums)
            
            out = listToString(ret)
            out_2 = listToString(ret_2)
            print(f"Solved using set:         {out}")
            print(f"Solved in constant space: {out_2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
