"""
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def trap(self, height: List[int]) -> int:
        l = r = water = 0
        for i in range(1, len(height)):
            if height[i] < height[i - 1]:
                r = i
                water += height[r] - height[l]
            elif height[i] > height[i - 1]:
                l = i
            else:
                pass
        return water


def main():
    while True:
        try:
            line = input()
            height = stringToList(line)
            
            sol = Solution()
            ret = sol.trap(height)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
