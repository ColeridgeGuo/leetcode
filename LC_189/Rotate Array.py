"""
    Given an array, rotate the array to the right by k steps, where k is
    non-negative.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def rotate_insert(self, nums: List[int], k: int) -> None:
        """
            Time Complexity: O(n*k)
            Space Complexity: O(1)
        """
        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop()
        return
    
    def rotate_brute_force(self, nums: List[int], k: int) -> None:
        """
            Time Complexity: O(n*k)
            Space Complexity: O(1)
        """
        for i in range(k):
            prev = nums[-1]
            for j in range(len(nums)):
                nums[j], prev = prev, nums[j]
        return
    
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
        return


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
            sol.rotate_insert(nums1, k)
            sol.rotate_brute_force(nums2, k)
            sol.rotate_extra_array(nums3, k)
            
            out_insert = listToString(nums1)
            out_brute_force = listToString(nums2)
            out_extra_array = listToString(nums3)
            print(f"Solved using .insert():  {out_insert}")
            print(f"Solved with brute force: {out_brute_force}")
            print(f"Solved with extra array: {out_extra_array}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
