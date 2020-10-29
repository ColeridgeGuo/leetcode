"""
Design a class to find the kth largest element in a stream. Note that it is the
kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an
integer array nums, which contains initial elements from the stream. For each
call to the method KthLargest.add, return the element representing the kth
largest element in the stream.
"""
from typing import List
from common_funcs import stringToList
import heapq


class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


def main():
    while True:
        try:
            operations = input()
            numbers = input()
            operations = stringToList(operations)
            numbers = stringToList(numbers)
            
            kthLargest = None
            res = []
            for i, op in enumerate(operations):
                if op == 'KthLargest':
                    kthLargest = KthLargest(*numbers[i])
                    res.append(None)
                elif op == 'add':
                    kth = kthLargest.add(numbers[i][0])
                    res.append(kth)
            print(res)
            
        except StopIteration:
            break


if __name__ == '__main__':
    main()
