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
        to the right of each number, i.e., prefix product and suffix product.
        Multiply the products at each position to achieve "product but self".
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = 1
        suffix[-1] = 1
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
            suffix[~i] = nums[~i + 1] * suffix[~i + 1]
        return [prefix[i] * suffix[i] for i in range(len(nums))]

    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        """
        Similar to method 1 but without using two extra arrays, but instead
        store the products in the output array directly in two passes.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = [0] * len(nums)
        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]
        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix_product
            suffix_product *= nums[i]
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
