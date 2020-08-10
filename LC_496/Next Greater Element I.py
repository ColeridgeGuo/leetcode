"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
elements are subset of nums2. Find all the next greater numbers for nums1's
elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to
its right in nums2. If it does not exist, output -1 for this number.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            n = len(nums1), m = len(nums2)
            Time Complexity: O(n*m) = O(m^2), n <= m
            Space Complexity: O(n)
        """
        res = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            idx = nums2.index(num)
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > num:
                    res[i] = nums2[j]
                    break
        return res

    def nextGreaterElement_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            n = len(nums1), m = len(nums2)
            Time Complexity: O(m)
            Space Complexity: O(m)
        """
        dic, stack = {}, []
        for num in nums2:
            while stack and stack[-1] < num:
                dic[stack.pop()] = num
            stack.append(num)
        return [dic.get(x, -1) for x in nums1]


def main():
    while True:
        try:
            line = input()
            nums1 = stringToList(line)
            line = input()
            nums2 = stringToList(line)

            sol = Solution()
            ret = sol.nextGreaterElement(nums1, nums2)
            ret2 = sol.nextGreaterElement_2(nums1, nums2)
            
            out = listToString(ret)
            out2 = listToString(ret2)
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
