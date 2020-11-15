"""
Given two strings s and t, return the number of distinct subsequences of s which
equals t.
A string's subsequence is a new string formed from the original string by
deleting some (can be none) of the characters without disturbing the relative
positions of the remaining characters. (i.e., "ACE" is a subsequence of "ABCDE"
while "AEC" is not).
It's guaranteed the answer fits on a 32-bit signed integer.
"""
from common_funcs import stringToString, stringToString_out


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        S[0:j] contains T[0:i] 'dp[i+1][j+1]' many times as distinct
        subsequences.
        
        Init: dp[0][j] = 1 for every j because an empty string is a subsequence
              of an empty string.
        Transition: dp[i+1][j+1] = dp[i+1][j] at least, meaning the number of
                    distinct subsequences we have if we skip S[j];
                    if T[i] == S[j], then we add dp[i][j] to it, meaning that in
                    addition to what we already have, we can include additional
                    matching subsequences from S[0:j-1] and T[0:i-1].
        The result will be dp[|T|][|S|].
        """
        dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
        for j in range(len(s)+1):
            dp[0][j] = 1
        for i in range(len(t)):
            for j in range(len(s)):
                dp[i+1][j+1] = dp[i+1][j]
                if t[i] == s[j]:
                    dp[i+1][j+1] += dp[i][j]
        return dp[len(t)][len(s)]


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            t = stringToString(line)
            
            sol = Solution()
            ret = sol.numDistinct(s, t)
            
            out = stringToString_out(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
