"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj)
such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in
the same order (i.e., an equal array).
"""
import collections
from typing import List
from common_funcs import stringToList


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # count the frequency of each row
        rows = collections.Counter(map(tuple, grid))
        # count the frequency of each column by creating the transpose of grid
        cols = collections.Counter(zip(*grid))
        # for equal row/col, multiply their frequencies to get number of pairs
        return sum(cols[pair] * rows[pair] for pair in rows)


def main():
    while True:
        try:
            line = input()
            grid = stringToList(line)

            sol = Solution()
            ret = sol.equalPairs(grid)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
