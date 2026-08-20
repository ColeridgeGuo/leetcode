"""
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course) # build adjacency list
            in_degrees[course] += 1 # build in-degree list

        # start with courses that have no prerequisites (nodes with 0 in-degree)
        from collections import deque
        queue = deque(
            course for course in range(numCourses) if in_degrees[course] == 0)

        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            for next_course in graph[course]:
                in_degrees[next_course] -= 1

                if in_degrees[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses


def main():
    while True:
        try:
            line = input()
            num = int(line)
            line = input()
            prereqs = stringToList(line)
            
            sol = Solution()
            ret = sol.canFinish(num, prereqs)
            
            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
