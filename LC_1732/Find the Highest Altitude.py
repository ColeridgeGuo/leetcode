"""
There is a biker going on a road trip. The road trip consists of n + 1 points at
different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in
altitude between points i and i + 1 for all (0 <= i < n).
Return the highest altitude of a point.
"""
import itertools
from typing import List
from common_funcs import stringToList


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = start = 0
        for g in gain:
            start += g
            ans = max(ans, start)
        return ans

    def largestAltitude_2(self, gain: List[int]) -> int:
        return max(itertools.accumulate(gain, initial=0))


def main():
    while True:
        try:
            line = input()
            gain = stringToList(line)

            sol = Solution()
            ret = sol.largestAltitude(gain)
            ret2 = sol.largestAltitude_2(gain)

            print(f"Solved with prefix sum:            {ret}")
            print(f"Solved with itertools' accumulate: {ret2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
