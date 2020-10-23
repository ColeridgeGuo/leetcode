"""
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def trap_memo(self, height: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not height:
            return 0
        water = 0
        n = len(height)
        l_max, r_max = [0] * n, [0] * n
        l_max[0], r_max[-1] = height[0], height[-1]
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i-1])
        for i in range(n - 2, -1, -1):
            r_max[i] = max(height[i], r_max[i+1])
        for i in range(1, n - 1):
            water += min(l_max[i], r_max[i]) - height[i]
        return water
    
    def trap_two_pointer(self, height: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not height:
            return 0
        water = 0
        n = len(height)
        left, right = 0, n-1
        l_max, r_max = height[0], height[-1]
        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            
            if l_max < r_max:
                water += l_max - height[left]
                left += 1
            else:
                water += r_max - height[right]
                right -= 1
        return water


def main():
    while True:
        try:
            line = input()
            height = stringToList(line)
            
            sol = Solution()
            ret_m = sol.trap_memo(height)
            ret_t = sol.trap_two_pointer(height)
            
            print(f"Solved using memoization:  {ret_m}")
            print(f"Solved using two pointers: {ret_t}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
