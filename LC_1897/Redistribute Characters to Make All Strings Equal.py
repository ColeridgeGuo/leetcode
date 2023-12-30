"""
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a
non-empty string, and move any character from words[i] to any position in
words[j].

Return true if you can make every string in words equal using any number of
operations, and false otherwise.
"""
import collections
from typing import List
from common_funcs import stringToList


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = collections.Counter(char for word in words for char in word)
        return any(counter[cnt] % len(words) for cnt in counter)


def main():
    while True:
        try:
            line = input()
            words = stringToList(line)

            sol = Solution()
            ret = sol.makeEqual(words)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
