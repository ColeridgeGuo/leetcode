"""
    Assume you are to give each of your children at most one cookie. Each child
    i has a greed factor g_i, which is the minimum size of a cookie that the
    child will be content with; and each cookie j has a size s_j. If s_j >= g_i,
    we can assign the cookie j to the child i, and the child i will be content.
    Your goal is to maximize the number of your content children and output the
    maximum number.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def findContentChildren_2(self, g: List[int], s: List[int]) -> int:
        """
            m = len(g), n = len(s)
            Time Complexity: O(m log(m)) + O(n log(n))
            Space Complexity: O(m + n)
        """
        g.sort()
        s.sort()
        child = cookie = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child


def main():
    while True:
        try:
            line = input()
            g = stringToList(line)
            line = input()
            s = stringToList(line)

            sol = Solution()
            ret = sol.findContentChildren_2(g, s)
            
            out = str(ret)
            print(f"Solved in O(n log(n)) time: {out}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
