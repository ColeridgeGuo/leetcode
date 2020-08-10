"""
Given a string which consists of lowercase or uppercase letters, find the length
of the longest palindromes that can be built with those letters. This is case
sensitive, for example "Aa" is not considered a palindrome here.
"""
from common_funcs import stringToString


class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        ans = 0
        for v in Counter(s).values():
            ans += v // 2 * 2
        return ans + 1 if ans < len(s) else ans


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.longestPalindrome(s)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
