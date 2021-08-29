"""
Given an integer array nums and an integer k, return the kth largest element in 
the array. Note that it is the kth largest element in the sorted order, not the 
kth distinct element.
"""
import heapq
import random
from typing import List

from common_funcs import stringToList


class Solution:
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        """
        Maintain a min-heap of k elements, push every number on the heap and pop 
        off the smallest number if size exceeds k, the top is the kth largest
        Time Complexity: O(n*log(k))
        Space Complexity: O(k)
        """
        minheap = []
        for n in nums:
            heapq.heappush(minheap, n)
            if len(minheap) > k:
                heapq.heappop(minheap)
        return minheap[0]

    def findKthLargest_qs(self, nums: List[int], k: int) -> int:
        """
        An implement of the randomized quick-select algorithm
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if len(nums) == 1:
            return nums[0]
        pivot = random.choice(nums)
        L = [x for x in nums if x < pivot]
        E = [x for x in nums if x == pivot]
        G = [x for x in nums if x > pivot]
        if k <= len(G):
            return self.findKthLargest_qs(G, k)
        elif k <= len(G) + len(E):
            return pivot
        else:
            return self.findKthLargest_qs(L, k - len(G) - len(E))


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.findKthLargest_heap(nums, k)
            ret2 = sol.findKthLargest_qs(nums, k)

            out = str(ret)
            out2 = str(ret2)
            print(f"Solved using min heap:     {out}")
            print(f"Solved using quick select: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
