"""
Given an array of intervals, merge all overlapping intervals, and return an 
array of the non-overlapping intervals that cover all the intervals in the input
"""
from typing import List
from common_funcs import listToString, stringToList


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort the intervals by start time and for each interval i, 
        - if curr ends after end_i, curr covers i entirely so we skip
        - if otherwise curr ends after start_i, enlarge curr's end to end_i
        - else if curr ends before start_i, no overlap so we add curr to res
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

    def merge_2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        curr = intervals[0]
        res = [curr]
        for interval in intervals:
            if interval[0] <= curr[1]:  # overlapping intervals
                curr[1] = max(curr[1], interval[1])
            else:  # disjoint intervals
                curr = interval
                res.append(curr)
        return res

    def merge_3(self, intervals: List[List[int]]) -> List[List[int]]:
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
