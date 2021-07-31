"""
Given an array of meeting time intervals where intervals[i] = [start_i, end_i], 
determine if a person could attend all meetings.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(intervals[i-1][1] <= intervals[i][0] for i in range(1, len(intervals)))
        # return not any(intervals[i-1][1] > intervals[i][0] for ...)


def main():
    while True:
        try:
            line = input()
            intervals = stringToList(line)

            sol = Solution()
            ret = sol.canAttendMeetings(intervals)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
