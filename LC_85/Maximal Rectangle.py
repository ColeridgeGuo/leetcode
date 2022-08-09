"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest 
rectangle containing only 1's and return its area.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def maximalRectangle_hist(self, matrix: List[List[str]]) -> int:
        """
        Treat each row w/ cells above it as a histogram, then use LC_84's method 
        to find the max rectangle area in this histogram, which is also the max 
        rectangle in the matrix so far.

        Time Complexity: O(n*m), n = # of rows, m = # of columns
        Space Complexity: O(m)
        """

        def maxAreaInHistogram(heights: List[int]) -> int:
            """
            Same as LC_84, finds the maximum rectangle area in a histogram
            """
            stack = [-1]
            res = 0
            for i in range(len(heights)):
                while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
            while stack[-1] != -1:
                h = heights[stack.pop()]
                w = len(heights) - stack[-1] - 1
                res = max(res, h * w)
            return res

        if not matrix:
            return 0
        res = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            res = max(res, maxAreaInHistogram(dp))
        return res

    def maximalRectangle_dp(self, matrix: List[List[str]]) -> int:
        """
        Find max rectangle by expanding to the left/right as far as possible and 
        multiplying the height to find the area.

        Time Complexity: O(n*m), n = # of rows, m = # of columns
        Space Complexity: O(m)
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        # initialize left/right as the leftmost/rightmost boundary possible
        left, right, height = [0] * n, [n] * n, [0] * n
        res = 0
        for i in range(m):
            curr_left, curr_right = 0, n
            # update height
            for j in range(n):
                height[j] = height[j] + 1 if matrix[i][j] == '1' else 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], curr_left)
                else:
                    left[j] = 0
                    curr_left = j + 1
            # update right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curr_right)
                else:
                    right[j] = n
                    curr_right = j
            # update the area
            for j in range(n):
                res = max(res, height[j] * (right[j] - left[j]))
        return res


def main():
    while True:
        try:
            line = input()
            matrix = stringToList(line)

            sol = Solution()
            ret = sol.maximalRectangle_hist(matrix)
            ret2 = sol.maximalRectangle_dp(matrix)

            out = str(ret)
            out2 = str(ret2)
            print(f"Solved by calculating max rectangle in histogram: {out}")
            print(f"Solved using dynamic programming:                 {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
