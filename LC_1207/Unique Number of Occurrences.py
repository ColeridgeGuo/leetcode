"""
Given an array of integers arr, return true if the number of occurrences of each
value in the array is unique or false otherwise.
"""
import collections
from typing import List
from common_funcs import stringToList


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = collections.Counter(arr)
        return len(set(freq.values())) == len(freq.values())


def main():
    while True:
        try:
            line = input()
            arr = stringToList(line)

            sol = Solution()
            ret = sol.uniqueOccurrences(arr)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
