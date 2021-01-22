"""
Given an array nums of n integers where n > 1,  return an array output such that
output[i] is equal to the product of all the elements of nums except nums[i].

Constraint: It's guaranteed that the product of the elements of any prefix or
suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not
count as extra space for the purpose of space complexity analysis.)
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Construct two arrays: the products of all the numbers to the left and
        to the right of each number. Multiply the products at each position to
        achieve "product but self".
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        L, R, res = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        L[0], R[-1] = 1, 1
        for i in range(1, len(nums)):
            L[i] = nums[i - 1] * L[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            R[i] = nums[i + 1] * R[i + 1]
        res = [L[i] * R[i] for i in range(len(nums))]
        return res
    
    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        """
        Similar to method 1 but without using two extra arrays, but instead
        store the products in the output array directly in two passes.
        """
        res = [0] * len(nums)
        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]
        R = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= R
            R *= nums[i]
        return res

def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret = sol.productExceptSelf(nums)
            ret2 = sol.productExceptSelf_2(nums)
            
            out = listToString(ret)
            out2 = listToString(ret2)
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
