"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing
moving one unit north, south, east,or west, respectively. You start at the
origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time
you are on a location you have previously visited. Return false otherwise.
"""
from common_funcs import stringToString


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        pos = (0, 0)
        visited = {pos}
        for p in path:
            pos = tuple(map(sum, zip(pos, directions[p])))
            if pos in visited:
                return True
            visited.add(pos)
        return False


def main():
    while True:
        try:
            line = input()
            path = stringToString(line)

            sol = Solution()
            ret = sol.isPathCrossing(path)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
