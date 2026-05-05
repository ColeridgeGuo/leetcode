"""
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Note: You may not slant the container and n is at least 2.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two-pointer approach: Start with the widest container.
        The area is limited by the shorter height. Moving the taller pointer
        can only decrease area (shorter height stays same, width decreases).
        Moving the shorter pointer might find a taller line, potentially
        increasing area despite the width decrease.
        
        Time complexity : O(n). Single pass.
        Space complexity : O(1). Constant space is used.
        """
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


def main():
    while True:
        try:
            line = input()
            height = stringToList(line)
            
            sol = Solution()
            ret = sol.maxArea(height)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
