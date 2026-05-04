"""
Given two strings s and p, return an array of all the start indices of p's
anagrams in s. You may return the answer in any order.
"""
from typing import List
from common_funcs import stringToString, listToString
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ans, p_len = [], len(p)
        p_count, window_count = Counter(p), Counter(s[:p_len])
        for i in range(len(s) - p_len + 1):
            if window_count == p_count:
                ans.append(i)
            if i + p_len < len(s):
                window_count[s[i + p_len]] += 1
                window_count[s[i]] -= 1
        return ans


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            p = stringToString(line)

            sol = Solution()
            ret = sol.findAnagrams(s, p)

            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
