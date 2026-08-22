"""
Given an array of intervals, merge all overlapping intervals, and return an 
array of the non-overlapping intervals that cover all the intervals in the input
"""
from typing import List
from common_funcs import listToString, stringToList


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort intervals by start time and compare each one with the current
        merged interval: skip covered intervals, extend overlaps, and append
        the current interval before starting a new disjoint group.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        curr = intervals[0][:]
        for i in range(len(intervals)):
            if curr[1] >= intervals[i][1]:  # [end, inf)
                continue
            elif curr[1] >= intervals[i][0]:  # [start, end)
                curr[1] = intervals[i][1]
            else:  # (-inf, start)
                res.append(curr)
                curr = intervals[i][:]
        res.append(curr)
        return res

    def merge_2(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Sort intervals by start time and keep the current merged interval in
        the result, extending its end for overlaps or appending a new interval
        when the next interval is disjoint.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        intervals = sorted(intervals, key=lambda interval: interval[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            last = merged[-1]
            if start <= last[1]: # overlapping intervals
                last[1] = max(last[1], end)
            else: # disjoint intervals
                merged.append([start, end])
        return merged

    def merge_3(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort intervals by start time and merge each overlap directly into the
        last result interval; otherwise, append the interval as a new group.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        res = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if res and interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res


def main():
    while True:
        try:
            line = input()
            intervals = stringToList(line)

            sol = Solution()
            ret = sol.merge(intervals)
            ret2 = sol.merge_2(intervals)
            ret3 = sol.merge_3(intervals)

            out = listToString(ret)
            out2 = listToString(ret2)
            out3 = listToString(ret3)
            print(out)
            print(out2)
            print(out3)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
