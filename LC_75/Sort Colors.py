"""
Given an array nums with n objects colored red, white, or blue, sort them 
in-place so that objects of the same color are adjacent, with the colors in the 
order red, white, and blue. We will use the integers 0, 1, and 2 to represent 
the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
"""
from typing import List
from common_funcs import listToString, stringToList


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Mimics counting sort: counting the number of occurrences of each color, 
        storing in an array with colors(0/1/2) being indices. Then re-populate 
        nums with 0/1/2 using each of their occurrences
        """
        # the number at index 0/1/2 represents the # of occurrences of 0/1/2
        colors = [0] * 3
        for n in nums:
            colors[n] += 1

        i = 0  # index of nums
        while i < len(nums):
            for color, count in enumerate(colors):
                for _ in range(count):
                    nums[i] = color
                    i += 1

    def sortColors_2(self, nums: List[int]) -> None:
        """
        This is the Dutch national flag problem. Keep two pointers for red(0) 
        and blue(2). Swap the current number with two if current is 2 and the 
        same for 0
        """
        zero, two = 0, len(nums) - 1
        for i in range(len(nums)):
            while nums[i] == 2 and i < two:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            while nums[i] == 0 and i > zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    def sortColors_3(self, nums: List[int]) -> None:
        """
        Similar to method 2, but with 3 pointers
        """
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1
        return


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            nums2 = stringToList(line)
            nums3 = stringToList(line)

            sol = Solution()
            sol.sortColors(nums)
            sol.sortColors_2(nums2)
            sol.sortColors_3(nums3)
            out = listToString(nums)
            out2 = listToString(nums2)
            out3 = listToString(nums3)
            print(f"Solved by counting:   {out}")
            print(f"Solved by swapping:   {out2}")
            print(f"Solved by swapping 2: {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
