"""
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        1. You can get maximum product by multiplying the current element with
        maximum product calculated so far (current element is positive).
        2. You can get maximum product by multiplying the current element with
        minimum product calculated so far (current element is negative).
        3. Current element might be a starting point for max product subarray
        """
        res = float('-inf')
        # imax and imin store the max/min product of subarray up to nums[i]
        imax = imin = 1
        for n in nums:
            a, b = imax * n, imin * n
            imax, imin = max(n, b, a), min(n, b, a)
            res = max(res, imax)  # update result to new imax if greater
        return res
    
    def maxProduct_2(self, nums: List[int]) -> int:
        """
        the subarray with max product must start with the 1st element, or end
        with the last element => max product must be prefix/suffix product. We
        then calculate the prefix and suffix product arrays and return the max.
        0 is like a delimiter, reset the product to 1
        """
        reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            reverse[i] *= reverse[i-1] or 1
        return max(nums + reverse)
    
    def maxProduct_3(self, nums: List[int]) -> int:
        """
        if there is an odd # of negative numbers, either the left or the right
        one should be included. Scanning from left to right, and from right to
        left in two passes would reveal the one to be included. 0 is like a
        delimiter, reset the product to 1
        """
        res, product = float('-inf'), 1
        for i in range(len(nums)):
            product *= nums[i]
            res = max(product, res)
            product = 1 if nums[i] == 0 else product
        product = 1
        for i in range(len(nums)):
            product *= nums[~i]
            res = max(product, res)
            product = 1 if nums[~i] == 0 else product
        return res


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            nums2 = stringToList(line)
            nums3 = stringToList(line)
            
            sol = Solution()
            ret = sol.maxProduct(nums)
            ret2 = sol.maxProduct_2(nums2)
            ret3 = sol.maxProduct_3(nums3)
            
            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            print(out)
            print(out2)
            print(out3)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
