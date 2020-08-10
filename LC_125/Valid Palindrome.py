"""
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.
"""
from common_funcs import stringToString


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        head = 0; tail = len(s) - 1
        while tail > head:
            while not s[head].isalnum():
                head += 1
                if head >= len(s): return True
            while not s[tail].isalnum():
                tail -= 1
                if tail <= 0: return True
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
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