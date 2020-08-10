"""
    Given two arrays, write a function to compute their intersection.
    Note:
        Each element in the result must be unique.
        The result can be in any order.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def intersection_sets(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            Time Complexity: O(n+m)
            Space Complexity: O(n+m)
        """
        return list(set(nums1).intersection(set(nums2)))
    
    def intersection_(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


def main():
    while True:
        try:
            line = input()
            nums1 = stringToList(line)
            line = input()
            nums2 = stringToList(line)
            
            sol = Solution()
            ret_sets = sol.intersection_sets(nums1, nums2)
            
            out_sets = listToString(ret_sets)
            print(f"Solved using set intersection: {out_sets}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
