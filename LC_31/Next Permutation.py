"""
Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible
order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        # find the first increasing pair from the end
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        # if nums is entirely non-increasing, reverse itself; otherwise,
        if i >= 0:
            # find the the number just larger than nums[i] and swap them
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # reverse the part to the right of i, which are non-increasing by
        # definition and reversing them would make them increasing, thus
        # creating the next permutation
        i, j = i + 1, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
        # the last four lines can be swapped with
        #   nums[i+1:] = nums[:i:-1] if i >= 0 else nums[::-1]
        # but potentially using more than constant extra memory


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            sol.nextPermutation(nums)
            
            out = listToString(nums)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
