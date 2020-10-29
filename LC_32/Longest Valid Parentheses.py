"""
Given a string containing just the characters '(' and ')', find the length of
the longest valid (well-formed) parentheses substring.
"""
from common_funcs import stringToString


class Solution:
    def longestValidParentheses_dp(self, s: str) -> int:
        """
        dp[i] is the length of the longest valid substring ending at ith index
        If s[i-1] = '(' and s[i] = ')', we can found a valid pair, dp[i-2] + 2
        If s[i-1] = ')' and s[i] = ')', we look for a '(' to close this ')' at
        index dp[i-1]-2
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        ans, dp = 0, [0]*len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2
                    dp[i] += dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0
                ans = max(dp[i], ans)
        return ans
    
    def longestValidParentheses_stack(self, s: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        ans, stack = 0, [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans

    def longestValidParentheses_pointer(self, s: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        ans = left = right = 0
        # scan from left to right
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:  # valid pair
                ans = max(ans, 2 * right)
            elif right > left:  # invalid pair, reset counters
                left = right = 0
                
        left = right = 0
        # scan from right to left
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:  # valid pair
                ans = max(ans, 2 * left)
            elif left > right:  # invalid pair, reset counters
                left = right = 0
        return ans


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            
            sol = Solution()
            ret_dp = sol.longestValidParentheses_dp(s)
            ret_s = sol.longestValidParentheses_stack(s)
            ret_c = sol.longestValidParentheses_pointer(s)
            
            out_dp = str(ret_dp)
            out_s = str(ret_s)
            out_c = str(ret_c)
            print(f"Solved using dynamic programming: {out_dp}")
            print(f"Solved using a stack:             {out_s}")
            print(f"Solved with constant space:       {out_c}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
