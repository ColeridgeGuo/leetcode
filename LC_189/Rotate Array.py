"""
    Given an array, rotate the array to the right by k steps, where k is
    non-negative.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    
    def rotate_brute_force(self, nums: List[int], k: int) -> None:
        """
        Manually move each element k steps to the right.
        Time Complexity: O(n*k)
        Space Complexity: O(1)
        """
        for i in range(k):
            prev = nums[-1]
            for j in range(len(nums)):
                nums[j], prev = prev, nums[j]
    
    def rotate_extra_array(self, nums: List[int], k: int) -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        temp = [0] * n
        for i in range(n):
            temp[(i+k) % n] = nums[i]
        nums[:] = temp

    def rotate_reverse(self, nums: List[int], k: int) -> None:
        """
        1. Reverse the entire array
        2. Then reverse the first k elements
        3. Finally, reverse the remaining n-k elements
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        def reverse(nums: List[int], start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)


def main():
    while True:
        try:
            line = input()
            nums1 = stringToList(line)
            nums2 = stringToList(line)
            nums3 = stringToList(line)
            line = input()
            k = int(line)
            
            sol = Solution()
            sol.rotate_brute_force(nums1, k)
            sol.rotate_extra_array(nums2, k)
            sol.rotate_reverse(nums3, k)
            
            out_brute_force = listToString(nums1)
            out_extra_array = listToString(nums2)
            out_reverse = listToString(nums3)
            print(f"Solved with brute force: {out_brute_force}")
            print(f"Solved with extra array: {out_extra_array}")
            print(f"Solved with reverse:     {out_reverse}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
