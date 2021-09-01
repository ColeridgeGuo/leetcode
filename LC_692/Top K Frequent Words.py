"""
Given an array of strings words and an integer k, return the k most frequent 
strings.

Return the answer sorted by the frequency from highest to lowest. Sort the 
words with the same frequency by their lexicographical order.
"""
import collections
import heapq
from typing import List

from common_funcs import listToString, stringToList


class Solution:
    def topKFrequent_sort(self, words: List[str], k: int) -> List[str]:
        """
        Count frequencies then sort by frequencies and break ties alphabetically
        Time Complexity: O(n*log(n))
        Space Complexity: O(n)
        """
        freq = collections.Counter(words)
        return sorted(freq, key=lambda x: (-freq[x], x))[:k]

    def topKFrequent_heap(self, words: List[str], k: int) -> List[str]:
        """
        Count frequencies then use minheap to return top k frequent elements
        Time Complexity: O(n*log(k))
        Space Complexity: O(k)
        """
        freq = collections.Counter(words)
        return heapq.nsmallest(k, freq, key=lambda x: (-freq[x], x))


def main():
    while True:
        try:
            line = input()
            words = stringToList(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.topKFrequent_sort(words, k)
            ret2 = sol.topKFrequent_heap(words, k)

            out = listToString(ret)
            out2 = listToString(ret2)
            print(f"Solved by sorting: {out}")
            print(f"Solved w/ minheap: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
