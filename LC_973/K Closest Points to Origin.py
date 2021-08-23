"""
Given an array of points where points[i] = [xi, yi] represents a point on the 
X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance 

You may return the answer in any order. The answer is guaranteed to be unique 
(except for the order that it is in).
"""
from typing import List
from common_funcs import listToString, stringToList


class Solution:
    def kClosest_sort(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Sort points on ascending Euclidean distance and pick the top k points
        Time Complexity: O(n*log(n))
        Space Complexity: O(n)
        """
        return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]

    def kClosest_pq(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Use heapq's nsmallest, implemented similarly to the 1st method (sort)
        Time Complexity: O(n*log(n))
        Space Complexity: O(n)
        """
        import heapq
        return heapq.nsmallest(k, points, key=lambda p: p[0]**2+p[1]**2)

    def kClosest_heap(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Keep a max heap of size k, push new points onto the heap and if its size 
        exceeds k then pop the farthest point, then the heap is guaranteed to 
        maintain top k closest points.
        Time Complexity: O(n*log(k))
        Space Complexity: O(k)
        """
        import heapq
        maxheap = []
        for x, y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(maxheap, (dist, x, y))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        return [(x, y) for _, x, y in maxheap]

    def kClosest_qs(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Implement quick select algorithm to find the k-th closest element. First 
        find the pivot of which all the points to its left are closer to origin 
        and all the points to its right are farther. Then check pivot's index 
        relative to k and update the search interval accordingly.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        def closer(p1: List[int], p2: List[int]) -> bool:
            return (p1[0]**2 + p1[1]**2) <= (p2[0]**2 + p2[1]**2)

        def partition(l: int, r: int) -> int:
            """ 
            Move all points closer to origin than pivot to the left of it, and 
            those farther to the right, 
            """
            p = l  # index for partition
            for i in range(l, r):
                if closer(points[i], points[r]):
                    points[p], points[i] = points[i], points[p]
                    p += 1
            points[p], points[r] = points[r], points[p]
            return p

        l, r = 0, len(points) - 1
        while l <= r:
            mid = partition(l, r)
            if mid == k:
                break
            if mid < k:
                l = mid + 1
            else:
                r = mid - 1
        return points[:k]


def main():
    while True:
        try:
            line = input()
            points = stringToList(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.kClosest_sort(points, k)
            ret2 = sol.kClosest_pq(points, k)
            ret3 = sol.kClosest_heap(points, k)
            ret4 = sol.kClosest_qs(points, k)

            out = listToString(ret)
            out2 = listToString(ret2)
            out3 = listToString(ret3)
            out4 = listToString(ret4)
            print(f"Solved by sorting first:                {out}")
            print(f"Solved using heapq's nsmallest:         {out2}")
            print(f"Solved by keeping a max heap of size k: {out3}")
            print(f"Solved using quick select:              {out4}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
