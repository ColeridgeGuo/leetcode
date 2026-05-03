"""
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.
"""
from common_funcs import stringToString


class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1
            if s[L].casefold() != s[R].casefold():
                return False
            L += 1
            R -= 1
        return True


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            
            ret = Solution().isPalindrome(s)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()