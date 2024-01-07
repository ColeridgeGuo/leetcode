"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size
2 where:
- answer[0] is a list of all distinct integers in nums1 which are not present in
nums2.
- answer[1] is a list of all distinct integers in nums2 which are not present in
nums1.
Note that the integers in the lists may be returned in any order.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def findDifference(self, nums1: List[int],
                       nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]


def main():
    while True:
        try:
            line = input()
            nums1 = stringToList(line)
            line = input()
            nums2 = stringToList(line)

            sol = Solution()
            ret = sol.findDifference(nums1, nums2)

            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
