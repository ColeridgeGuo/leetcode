"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between
two words. The returned string should only have a single space separating the
words. Do not include any extra spaces.
"""
import collections
import re

from common_funcs import stringToString


class Solution:
    def reverseWords(self, s: str) -> str:
        words = re.split(r'\s+', s.strip())
        return ' '.join(reversed(words))

    def reverseWords_2(self, s: str) -> str:
        ans = collections.deque()
        word = []
        for i in range(len(s)+1):
            if i < len(s) and s[i] != ' ':
                word.append(s[i])
            elif word:
                ans.appendleft(''.join(word))
                word.clear()

        return ' '.join(ans)


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.reverseWords(s)
            ret2 = sol.reverseWords_2(s)

            print(f"Solved by re.split():           {ret}")
            print(f"Solved by scanning whitespaces: {ret2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
