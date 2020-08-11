"""
Given an input string (s) and a pattern (p), implement regular expression
matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""
from common_funcs import stringToString


class Solution:
    def isMatch_recursive(self, s: str, p: str) -> bool:
        """
        S = len(s), P = len(P)
        Time Complexity: O((S+P) * 2^(S+P/2))
        Space Complexity: O(S^2 + P^2)
        """
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch_recursive(s, p[2:]) or \
                   first_match and self.isMatch_recursive(s[1:], p)
        else:
            return first_match and self.isMatch_recursive(s[1:], p[1:])
        
    def isMatch_memo(self, s: str, p: str) -> bool:
        """
        S = len(s), P = len(P)
        Time Complexity: O(SP)
        Space Complexity: O(SP)
        """
        memo = {}
        
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)
                memo[i, j] = ans
            return memo[i, j]
        
        return dp(0, 0)
    
    def isMatch_dp(self, s: str, p: str) -> bool:
        """
            S = len(s), P = len(P)
            Time Complexity: O(SP)
            Space Complexity: O(SP)
        """
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            p = stringToString(line)
            
            sol = Solution()
            ret_r = sol.isMatch_recursive(s, p)
            ret_m = sol.isMatch_memo(s, p)
            ret_d = sol.isMatch_dp(s, p)
            
            print(f"Solved recursively:      {ret_r}")
            print(f"Solved with memoization: {ret_m}")
            print(f"Solved using DP:         {ret_d}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
