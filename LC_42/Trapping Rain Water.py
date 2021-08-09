"""
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def trap_memo(self, height: List[int]) -> int:
        """
        Use l_max and r_max to store the max height bar from the left/right up 
        to index i. For any index i, the water that can it trap is determined by 
        the shorter of the left and right max height bars. 
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        water, n = 0, len(height)
        # initialize the left end bar to be the highest on the left and the
        # right end to be the highest bar on the right
        l_max, r_max = [height[0]] * n, [height[-1]] * n
        # the highest bar to the left of index i
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i-1])
        # the highest bar to the right of index i
        for i in range(1, n):
            r_max[~i] = max(height[~i], r_max[~i+1])
        # calculate trapped water for each index
        for i in range(1, n-1):
            water += min(l_max[i], r_max[i]) - height[i]
        return water

    def trap_two_pointer(self, height: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        water = 0
        n = len(height)
        left, right = 0, n-1
        l_max, r_max = height[left], height[right]
        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max <= r_max:
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
