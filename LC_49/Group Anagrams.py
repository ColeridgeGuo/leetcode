"""
Given an array of strings strs, group the anagrams together. You can return the 
answer in any order.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return list(d.values())


def main():
    while True:
        try:
            line = input()
            strs = stringToList(line)

            sol = Solution()
            ret = sol.groupAnagrams(strs)

            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
