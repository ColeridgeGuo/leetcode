"""
A message containing letters from A-Z can be encoded into numbers using the
following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back
into letters using the reverse of the mapping above.

For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into
'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
"""
from common_funcs import stringToString


class Solution:
    def numDecodings_bt(self, s: str) -> int:
        """
        Backtracking to find all possible ways to decode.
        Time Complexity: O(2^n)
        Space Complexity: O(n)
        """
        def backtrack(i: int) -> int:
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            ways = backtrack(i+1)
            if i < len(s) - 1 and int(s[i:i+2]) <= 26:
                ways += backtrack(i+2)
            return ways

        return backtrack(0)

    def numDecodings_dp(self, s: str) -> int:
        """
        dp[i] represents the number of ways to decode at index i of s
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(s)
        dp = [0] * n + [1]
        for i in range(n-1, -1, -1):
            if s[i] != '0':
                dp[i] += dp[i+1]
                if i < n - 1 and int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]
        return dp[0]


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.numDecodings_bt(s)
            ret2 = sol.numDecodings_dp(s)

            print(f"Solved by backtracking:        {ret}")
            print(f"Solved by dynamic programming: {ret2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
