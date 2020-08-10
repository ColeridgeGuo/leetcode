"""
Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.
"""
from common_funcs import stringToString, stringToString_out


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expandAroundCenter(s: str, left: int, right: int) -> int:
            L, R = left, right
            while L >= 0 and R < len(s) and s[L] == s[R]:
                # expand around center if palindrome
                L -= 1
                R += 1
            return R - L - 1  # return found palindrome length
            
        if not s:
            return s
        start = end = 0
        for i in range(len(s)):
            # expand around single char to find odd-length palindrome
            len1 = expandAroundCenter(s, i, i)
            # expand around double chars to find even-length palindrome
            len2 = expandAroundCenter(s, i, i + 1)
            # adjust start and end according to the max palindrome length found
            max_len = max(len1, len2)
            if max_len > end - start:
                # move start and end to 1/2 max_len regardless of odd/even len
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end+1]

    def longestPalindrome_dp(self, s: str) -> str:
        n = len(s)
        res = ''
        # dp[i][j] indicates whether substring substring s(i, j) is palindrome
        dp = [[0]*n for _ in range(n)]

        # keep increasing the possible palindrome string
        for i in range(n-1, -1, -1):
            # find the max palindrome within this window of (i,j)
            for j in range(i, n):
                
                # check if substring between (i,j) is palindrome
                # - chars at i and j should match, and
                # - if j - i < to 3, just end chars should match, e.g.,
                #   if i == j, dp[i][j] = s[i] == s[j] (single char)
                #   i+1 == j, dp[i][j] = s[i] == s[j] (two same chars)
                #   i+2 == j , dp[i][j] = s[i] == s[j] (middle doesn't matter)
                # - if j - i >= 3, substring (i+1, j-1) should be palindrome too
                #   dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
                
                # update max palindrome string if current substring (i,j) is a
                # palindrome and only when necessary
                # (palindrome is not set or new palindrome is longer)
                if dp[i][j] and (not res or j - i + 1 > len(res)):
                    res = s[i:j+1]
        return res


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            
            sol = Solution()
            ret = sol.longestPalindrome(s)
            ret_dp = sol.longestPalindrome_dp(s)
            
            out = stringToString_out(ret)
            out_dp = stringToString_out(ret_dp)
            print(f"Solved by expanding around center for every char: {out}")
            print(f"Solved using dynamic programming:                 {out_dp}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
