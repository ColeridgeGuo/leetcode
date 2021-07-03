"""
Given a set of non-overlapping intervals, insert a new interval into the 
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start 
times.
"""
from typing import List
from common_funcs import listToString, stringToList


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Binary search for the position to insert newInterval and use methods in 
        Merge Intervals to merge overlapping intervals
        """
        res = []
        from bisect import insort
        insort(intervals, newInterval)
        for interval in intervals:
            if res and interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res

    def insert_2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        First add all intervals to the left of newInterval w/o overlaps; then 
        for any overlapping interval, merge them w/ newInterval; lastly add all 
        non-overlapping intervals to the right
        """
        res = []
        i = 0
        # add all intervals ending before newInterval starts
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # merge overlapping intervals including newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]),
                           max(newInterval[1], intervals[i][1])]
            i += 1
        res.append(newInterval)
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res

    def insert_3(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Similar to method 2, only with list comprehension
        """
        left = [i for i in intervals if i[1] < newInterval[0]]
        right = [i for i in intervals if i[0] > newInterval[1]]
        if len(left) + len(right) != len(intervals):
            newInterval = [min(newInterval[0], intervals[len(left)][0]),
                           max(newInterval[1], intervals[~len(right)][1])]
        return left + [newInterval] + right


def main():
    while True:
        try:
            line = input()
            intervals = stringToList(line)
            intervals2 = stringToList(line)
            intervals3 = stringToList(line)
            line = input()
            newInterval = stringToList(line)

            sol = Solution()
            ret = sol.insert(intervals, newInterval)
            ret2 = sol.insert_2(intervals2, newInterval)
            ret3 = sol.insert_3(intervals3, newInterval)

            out = listToString(ret)
            out2 = listToString(ret2)
            out3 = listToString(ret3)
            print(f"Solved using bisect's insort:                 {out}")
            print(f"Solved by adding each group:                  {out2}")
            print(f"Solved using list comprehension similar to 2: {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
