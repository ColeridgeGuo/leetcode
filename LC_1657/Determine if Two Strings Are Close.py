"""
Two strings are considered close if you can attain one from the other using the
following operations:

- Operation 1: Swap any two existing characters.
    - For example, abcde -> aecdb
- Operation 2: Transform every occurrence of one existing character into another
    existing character, and do the same with the other character.
    - For example, aacabb -> bbcbaa (all a's turn into b's,
        and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close,
and false otherwise.
"""
import collections

from common_funcs import stringToString


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        The numbers of occurrences and the letters themselves do not change no
        matter what operation is done.
        """
        freq1 = collections.Counter(word1)
        freq2 = collections.Counter(word2)
        occurrence_freq1 = collections.Counter(freq1.values())
        occurrence_freq2 = collections.Counter(freq2.values())
        return freq1.keys() == freq2.keys() and occurrence_freq1 == occurrence_freq2


def main():
    while True:
        try:
            line = input()
            word1 = stringToString(line)
            line = input()
            word2 = stringToString(line)

            sol = Solution()
            ret = sol.closeStrings(word1, word2)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
