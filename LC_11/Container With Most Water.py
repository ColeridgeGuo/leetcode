"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Time complexity : O(n). Single pass.
        Space complexity : O(1). Constant space is used.
        
        You have two heights H_left and H_right, and H_right < H_left, then we
        know we have two choices, we want to move one of them. If we move the
        larger one, we cannot increase the height for the simple reason that we
        are always limited by the shortest, and we would be decreasing j-i, the
        width as well.
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
