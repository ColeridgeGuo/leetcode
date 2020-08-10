"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should
be O(log (m+n)). You may assume nums1 and nums2 cannot be both empty.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            # make sure nums2 is always longer than nums1
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)  # lengths of two arrays
        # half_len is the total len // 2, this is the length of both the
        # combined left partitions and the combined right partitions
        lo, hi, half_len = 0, m, (m + n + 1) // 2
        
        while lo <= hi:
            i = (lo + hi) // 2  # index to partition nums1
            j = half_len - i    # index to partition nums2
            
            if i < m and nums2[j - 1] > nums1[i]:
                # we are too far to the left in nums1, need to move lo right to
                # give left partition of nums1 more elements
                lo = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # we are too far the right in nums1, need to move hi left to
                # give left partition of nums1 less elements
                hi = i - 1
            else:  # we have found the correct split
                
                if i == 0:  # if no left partition in nums1
                    max_of_left = nums2[j - 1]
                elif j == 0:  # if no left partition in nums2
                    max_of_left = nums1[i - 1]
                else:  # max_of_left is the max of two left partitions
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                
                if (m + n) % 2:  # if total length is odd, return middle number
                    return max_of_left
                
                # if total length is even, return avg of middle two numbers
                if i == m:  # if no right partition in nums1
                    min_of_right = nums2[j]
                elif j == n:  # if no right partition in nums2
                    min_of_right = nums1[i]
                else:  # min_of_right is the min of two right partitions
                    min_of_right = min(nums1[i], nums2[j])
                
                # if total length is even, return avg of the middle two numbers
                return (max_of_left + min_of_right) / 2


def main():
    while True:
        try:
            line = input()
            nums1 = stringToList(line)
            line = input()
            nums2 = stringToList(line)
            
            sol = Solution()
            ret = sol.findMedianSortedArrays(nums1, nums2)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
