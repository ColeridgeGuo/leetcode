"""
Given two arrays, write a function to compute their intersection.
Note:
    Each element in the result should appear as many times as it shows in both
    arrays. The result can be in any order.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def intersect_counter(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        return list((Counter(nums1) & Counter(nums2)).elements())
    
    def intersect_pointers(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            Time Complexity: O(n lg n)
            Space Complexity: O(n)
        """
        nums_1, nums_2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []
        while True:
            try:
                if nums_1[pt1] > nums_2[pt2]:
                    pt2 += 1
                elif nums_1[pt1] < nums_2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums_1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break
        return res


def main():
    while True:
        try:
            line = input()
            nums1 = stringToList(line)
            line = input()
            nums2 = stringToList(line)

            sol = Solution()
            ret_ct = sol.intersect_counter(nums1, nums2)
            ret_pt = sol.intersect_pointers(nums1, nums2)
            
            out_counter = listToString(ret_ct)
            out_pt = listToString(ret_pt)
            print(f"Solved using Python's Counter: {out_counter}")
            print(f"Solved using two pointers:     {out_pt}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
