"""
Given an array of integers heights representing the histogram's bar height where 
the width of each bar is 1, return the area of the largest rectangle in the 
histogram.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def largestRectangleArea_bf(self, heights: List[int]) -> int:
        """
        Find max area for every pair of bars with each updated min_height
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        res = 0
        for i in range(len(heights)):
            min_height = float('inf')
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                res = max(res, min_height * (j - i + 1))
        return res

    def largestRectangleArea_dc(self, heights: List[int]) -> int:
        """
        Divide the array into two parts at the shortest bar, then the max area 
        rectangle lies either to the left or right of the shortest bar, or is 
        formed by the shortest bar extended to the boundaries.
        Time Complexity: O(n*log(n)) average, O(n^2) worst case
        Space Complexity: O(n)
        """
        def calc_area(l: int, r: int) -> int:
            if l > r:
                return 0
            min_index = l
            for i in range(l, r+1):
                if heights[i] < heights[min_index]:
                    min_index = i
            return max(heights[min_index] * (r - l + 1),
                       calc_area(l, min_index - 1),
                       calc_area(min_index + 1, r))
        return calc_area(0, len(heights) - 1)

    def largestRectangleArea_stk(self, heights: List[int]) -> int:
        """
        Loop thru the histogram and maintain a monotonic stack of indices of 
        non-decreasing values because a non-decreasing value means that we can 
        extend to form a larger rectangle, whereas a smaller value means that we 
        have to pop off of the stack to calculate the max rectangle area so far. 
        Indices on the stack represent the index from which we start to build 
        the rectangle.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        heights_ = heights + [0]
        stack = [-1]
        res = 0
        for i in range(len(heights_)):
            while stack and heights_[i] < heights_[stack[-1]]:
                h = heights_[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res


def main():
    while True:
        try:
            line = input()
            heights = stringToList(line)

            sol = Solution()
            ret = sol.largestRectangleArea_bf(heights)
            ret2 = sol.largestRectangleArea_dc(heights)
            ret3 = sol.largestRectangleArea_stk(heights)

            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            print(f"Solved with brute force:      {out}")
            print(f"Solved with divide & conquer: {out2}")
            print(f"Solved using monotonic stack: {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
