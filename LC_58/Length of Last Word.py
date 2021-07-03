"""
Given a string s consists of some words separated by spaces, return the length 
of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.
"""
from common_funcs import stringToString


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(' ')[-1])

    def lengthOfLastWord_2(self, s: str) -> int:
        """
        Start from the back and move forward. Don't start counting until seeing 
        the first non-space character
        """
        res, tail = 0, len(s) - 1
        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        while tail >= 0 and s[tail] != ' ':
            res += 1
            tail -= 1
        return res


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            s2 = stringToString(line)

            sol = Solution()
            ret = sol.lengthOfLastWord(s)
            ret2 = sol.lengthOfLastWord_2(s2)

            out = str(ret)
            out2 = str(ret2)
            print(f"Solved using split(): {out}")
            print(f"Solved back to front: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
