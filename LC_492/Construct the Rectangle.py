"""
Given a specific rectangular web page’s area, your job by now is to design a
rectangular web page, whose length L and width W satisfy the following
requirements:
1. The width W should not be larger than the length L, which means L >= W.
2. The difference between length L and width W should be as small as possible.
"""
from typing import List
from common_funcs import listToString


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        """
            Construct rectangles for all divisors of area starting from 1, and
            find the optimal one.
            Time Complexity: O(sqrt(n)) - Time limit exceeded.
            Space Complexity: O(1)
        """
        res = [area, 1]
        for L in range(1, int(area ** 1/2) + 1):
            W, r = divmod(area, L)
            if r == 0 and L >= W:
                if L - W < res[0] - res[1]:
                    res = [L, W]
        return res

    def constructRectangle_2(self, area: int) -> List[int]:
        """
            Construct rectangles for all divisors of area starting from
            sqrt(area), and find the optimal one.
            Time Complexity: O(sqrt(n)) - (worst-case: prime numbers)
            Space Complexity: O(1)
        """
        L = int(area ** (1/2))
        while True:
            W, r = divmod(area, L)
            if r == 0 and L >= W:
                return [L, W]
            L += 1
            
    def constructRectangle_3(self, area: int) -> List[int]:
        W = int(area ** (1/2))
        while area % W:
            W -= 1
        return [area//W, W]


def main():
    while True:
        try:
            line = input()
            area = int(line)

            sol = Solution()
            ret = sol.constructRectangle(area)
            ret2 = sol.constructRectangle_2(area)
            ret3 = sol.constructRectangle_3(area)
            
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
