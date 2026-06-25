"""
Given an array of integers citations where citations[i] is the number of
citations a researcher received for their ith paper, return the researcher's
h-index.

The h-index is the maximum value of h such that the researcher has published at
least h papers that have each been cited at least h times.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Sort citations from highest to lowest, then count how many papers can
        satisfy each candidate h-index as the index grows.
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations, start=1):
            if i <= c:
                h = i
        return h

    def hIndex2(self, citations: List[int]) -> int:
        """
        Sort citations in ascending order, then find the first position where
        the remaining paper count is no greater than the citation count.
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        citations.sort()
        n = len(citations)
        for i, c in enumerate(citations):
            if n - i <= c:
                return n - i
        return 0

    def hIndex3(self, citations: List[int]) -> int:
        """
        Count papers by citation bucket, grouping all counts above n together,
        then scan h from high to low until at least h papers have h citations.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(citations)
        counts = [0 for _ in range(n + 1)]
        for c in citations:
            # papers with more than n citations fall under bucket n
            counts[min(c, n)] += 1
        papers = 0
        for h in range(n, -1, -1):
            papers += counts[h]
            if papers >= h:
                return h
        return 0


def main():
    while True:
        try:
            line = input()
            citations = stringToList(line)
            citations2 = stringToList(line)
            citations3 = stringToList(line)

            sol = Solution()
            ret = sol.hIndex(citations)
            ret2 = sol.hIndex2(citations2)
            ret3 = sol.hIndex3(citations3)

            print(f"Solved by sorting reversed: {ret}")
            print(f"Solved by sorting:          {ret2}")
            print(f"Solved by counting sort:    {ret3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
