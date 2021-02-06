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
        adjacency: List[List[int]] = [[] for _ in range(numCourses)]
        in_degrees = [0 for _ in range(numCourses)]
        for c1, c2 in prerequisites:
            adjacency[c1].append(c2)  # build adjacency list
            in_degrees[c2] += 1  # build in-degree list
        from collections import deque
        queue, visited = deque(), set()
        # find nodes with in-degree 0 (the nodes to start with)
        for i, dg in enumerate(in_degrees):
            if not dg:
                queue.append(i)
        # loop all the nodes whose in-degree is 0
        while queue:
            idx = queue.popleft()
            visited.add(idx)
            for edge in adjacency[idx]:
                in_degrees[edge] -= 1
                if not in_degrees[edge]:
                    queue.append(edge)
        return len(visited) == numCourses


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
