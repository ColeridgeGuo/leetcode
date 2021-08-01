"""
Given an array of meeting time intervals intervals where intervals[i] = 
[start_i, end_i], return the minimum number of conference rooms required.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Sort start and end times separately. A new room needs to be allocated if 
        one event starts before any already started event ends. Pointer e points 
        to the last finished event, and its room can be assigned to the next 
        non-overlapping event; otherwise a new room is needed
        """
        start_times, end_times = (sorted(l) for l in zip(*intervals))
        e = num_rooms = 0
        for s in range(len(start_times)):
            if start_times[s] < end_times[e]:
                num_rooms += 1
            else:
                e += 1
        return num_rooms

    def minMeetingRooms_2(self, intervals: List[List[int]]) -> int:
        """
        Sort start and end times altogether, add one room when events start and 
        close one room when events end, record the max number of room needed
        """
        res = curr_room_cnt = 0
        for _, sign in sorted(w for i in intervals for w in ((i[0], 1), (i[1], -1))):
            curr_room_cnt += sign  # +1 for start time; -1 for end time
            res = max(res, curr_room_cnt)
        return res

    def minMeetingsRooms_3(self, intervals: List[List[int]]) -> int:
        """
        Sort the events by start time and maintain a min heap of the end times 
        of current events. A new event requires a new room if it starts before 
        the earliest ending event; otherwise no new room is required and we 
        replace it with the new event's ending time. Min heap properties make it 
        O(1) time to check the earliest ending event.
        """
        import heapq
        # min heap of end times
        free_rooms = []
        # sort events by start time
        intervals.sort(key=lambda x: x[0])
        # push first event's end time onto min heap
        heapq.heappush(free_rooms, intervals[0][1])

        # process each following event
        for i in range(1, len(intervals)):
            # if new event starts after the earliest ending event
            if free_rooms[0] <= intervals[i][0]:
                heapq.heappop(free_rooms)  # remove the earliest ending event
            # put new event's end time onto min heap
            heapq.heappush(free_rooms, intervals[i][1])
        # number of events being held means the number of rooms required
        return len(free_rooms)


def main():
    while True:
        try:
            line = input()
            intervals = stringToList(line)

            sol = Solution()
            ret = sol.minMeetingRooms(intervals)
            ret2 = sol.minMeetingRooms_2(intervals)
            ret3 = sol.minMeetingsRooms_3(intervals)

            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            print(f"Solved w/ chronological ordering:   {out}")
            print(f"Solved w/ chronological ordering 2: {out2}")
            print(f"Solved with min heap:               {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
