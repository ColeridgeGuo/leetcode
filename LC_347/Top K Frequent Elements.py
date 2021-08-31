"""
Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.
"""
import collections
import heapq
import random
import itertools
from typing import List

from common_funcs import listToString, stringToList


class Solution:
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return heapq.nlargest(k, count, key=count.get)

    def topKFrequent_qs(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        unique = list(count.keys())

        def partition(left: int, right: int, pivot: int) -> int:
            pivot_frequency = count[unique[pivot]]
            # 1. move pivot to end
            unique[pivot], unique[right] = unique[right], unique[pivot]
            # 2. move all less frequent elements to the left
            store = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store], unique[i] = unique[i], unique[store]
                    store += 1
            # 3. move pivot to its final place
            unique[right], unique[store] = unique[store], unique[right]
            return store

        def quickselect(left: int, right: int, k_smallest: int) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place. 
            """
            # base case: the list contains only one element
            if left == right:
                return
            # select a random pivot_index
            pivot_index = random.randint(left, right)
            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)
            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array.
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.
        quickselect(0, len(unique) - 1, len(unique) - k)
        # Return top k frequent elements
        return unique[-k:]

    def topKFrequent_bs(self, nums: List[int], k: int) -> List[int]:
        """
        The frequency of any element is at most N so we use a bucket 
        representing frequencies 1~N and put in each element reversely to return 
        the top k most frequent elements.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        buckets = [[] for _ in range(len(nums)+1)]
        count = collections.Counter(nums).items()
        for num, freq in count:
            buckets[~freq].append(num)
        flattened = list(itertools.chain.from_iterable(buckets))
        return flattened[:k]


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.topKFrequent_heap(nums, k)
            ret2 = sol.topKFrequent_qs(nums, k)
            ret3 = sol.topKFrequent_bs(nums, k)

            out = listToString(ret)
            out2 = listToString(ret2)
            out3 = listToString(ret3)
            print(f"Solved using heap:         {out}")
            print(f"Solved using quick-select: {out2}")
            print(f"Solved using bucket sort:  {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
