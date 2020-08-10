"""
    You are to design a standard heater with fixed warm radius to warm all the
    houses. You are given positions of houses and heaters on a horizontal line,
    find out minimum radius of heaters so that all houses could be covered by
    those heaters.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        htr = min_radius = 0
        for house in sorted(houses):
            while htr < len(heaters) - 1 and \
                    abs(heaters[htr+1] - house) <= abs(heaters[htr] - house):
                htr += 1
            min_radius = max(min_radius, abs(heaters[htr] - house))
        return min_radius
    
    def findRadius_bs(self, houses: List[int], heaters: List[int]) -> int:
        from bisect import bisect_left
        heaters.sort()
        r = 0
        for h in houses:
            idx = bisect_left(heaters, h)  # insert pos for two closest heaters
            if idx == len(heaters):
                # insert after last heater
                r = max(r, h - heaters[-1])
            elif idx == 0:
                # insert before first heater
                r = max(r, heaters[0] - h)
            else:
                # insert in the middle, radius is wrt the closer heater
                r = max(r, min(heaters[idx] - h, h - heaters[idx - 1]))
        return r


def main():
    while True:
        try:
            line = input()
            houses = stringToList(line)
            line = input()
            heaters = stringToList(line)

            sol = Solution()
            ret = sol.findRadius(houses, heaters)
            ret_bs = sol.findRadius_bs(houses, heaters)
            
            out = str(ret)
            out_bs = str(ret_bs)
            print(f"Solved iteratively:         {out}")
            print(f"Solved using binary search: {out_bs}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
