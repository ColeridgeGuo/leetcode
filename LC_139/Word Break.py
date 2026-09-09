"""
Given a string s and a dictionary of strings wordDict, return whether s can be
segmented into a space-separated sequence of one or more dictionary words.
"""
from typing import List

from common_funcs import stringToList, stringToString


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[-1]

def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            wordDict = stringToList(line)

            sol = Solution()
            ret = sol.wordBreak(s, wordDict)

            out = str(ret)
            print(out)
        except EOFError:
            break


if __name__ == '__main__':
    main()
