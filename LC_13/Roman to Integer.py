"""
Given a roman numeral, convert it to an integer.
"""
from common_funcs import stringToString


class Solution:

    def romanToInt(self, s: str) -> int:
        """
        Roman numerals are usually written largest to smallest from left to 
        right, except when I(1), X(10), or C(100) come before a larger number to 
        denote that they are subracted to form 4, 9, 40, 90, etc. We read from 
        right to left, subtract the current number if it comes before a larger 
        one, add it otherwise.
        """
        lookup = dict(zip('IVXLCDM', [1, 5, 10, 50, 100, 500, 1000]))
        res = 0
        i, prev = len(s) - 1, s[-1]
        while i >= 0:
            if lookup[s[i]] < lookup[prev]:
                res -= lookup[s[i]]
            else:
                res += lookup[s[i]]
            prev = s[i]
            i -= 1
        return res


def main():
    while True:
        try:
            line = input()
            nums = stringToString(line)

            sol = Solution()
            ret = sol.romanToInt(nums)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
