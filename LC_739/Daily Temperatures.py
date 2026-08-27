"""
Given a list of daily temperatures, return the number of days to wait after
each day for a warmer temperature. If there is no future warmer day, use 0.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Keep unresolved day indices in a decreasing-temperature stack. When a
        warmer day appears, pop each colder day and record the wait distance.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        answer = [0] * len(temperatures)

        for day, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = day - prev_day
            stack.append(day)
        return answer


def main():
    while True:
        try:
            line = input()
            temperatures = stringToList(line)

            sol = Solution()
            ret = sol.dailyTemperatures(temperatures)

            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
