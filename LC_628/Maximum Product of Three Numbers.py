"""
Given an integer array, find three numbers whose product is maximum and output
the maximum product.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        min1 = min2 = 1000
        max1 = max2 = max3 = -1000
        for n in nums:
            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n
        return max(min1 * min2 * max1, max1 * max2 * max3)
    
    def maximumProduct_sort(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n*log(n))
        Space Complexity: O(n)
        """
        s = sorted(nums)
        return max(s[0] * s[1] * s[-1], s[-1] * s[-2] * s[-3])

    def maximumProduct_heapq(self, nums):
        import heapq
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.maximumProduct(nums)
            ret_s = sol.maximumProduct_sort(nums)
            ret_h = sol.maximumProduct_heapq(nums)
            
            out = str(ret)
            out_s = str(ret_s)
            out_h = str(ret_h)
            print(f"Solved in one single pass: {out}")
            print(f"Solved by sorting first:   {out_s}")
            print(f"Solved using heapq:        {out_h}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
