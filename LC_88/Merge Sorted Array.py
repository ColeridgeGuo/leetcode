"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing
order, and two integers m and n, representing the number of elements in nums1
and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should be stored inside nums1. Do not return anything, 
modify nums1 in-place instead.

"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Two pointers approach. Start two pointers from the end of the valid
        numbers, always write the larger of the two to the end of the array.
        Update the pointers accordingly.

        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        p1 = m - 1 # pointer to nums1 starting from the end
        p2 = n - 1 # pointer to nums2 starting from the end
        write = m + n - 1 # write pointer to put the larger numbers

        # stop when p2 reaches the beginning
        while p2 >= 0:
            # put nums1[p1] if p1 is still valid and it's larger
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else: # otherwise put nums2[p2] in nums1
                nums1[write] = nums2[p2]
                p2 -= 1
            write -= 1 # move write pointer to the left by 1



def main():
    while True:
        try:
            line = input()
            nums1 = stringToList(line)
            line = input()
            m = int(line)
            line = input()
            nums2 = stringToList(line)
            line = input()
            n = int(line)

            sol = Solution()
            sol.merge(nums1, m, nums2, n)

            out = listToString(nums1)
            print(f"Merged array: {out}")
        except (EOFError, StopIteration):
            break


if __name__ == '__main__':
    main()
