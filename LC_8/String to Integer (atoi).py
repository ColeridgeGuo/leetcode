"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the
first non-whitespace character is found. Then, starting from this character,
takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral
number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid
integral number, or if no such sequence exists because either str is empty or it
contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
"""
from common_funcs import stringToString


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        if not s[0].isnumeric() and s[0] not in {'+', '-'}:
            return 0
        res = []
        for c in s:
            if res and not c.isnumeric():
                break
            res.append(c)
        res = ''.join(res)
        try:
            res = int(''.join(res))
        except ValueError:
            return 0
        else:
            if res > 2**31 - 1:
                return 2**31 - 1
            if res < -2**31:
                return -2**31
            return res
        
    def myAtoi_re(self, s: str) -> int:
        import re
        match = re.match(r'^\s*([+-]?\d+)', s)
        if not match:
            return 0
        res = int(match.group(1))
        return min(2 ** 31 - 1, max(res, -2 ** 31))


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            
            sol = Solution()
            ret = sol.myAtoi(s)
            ret_r = sol.myAtoi_re(s)
            
            print(f"Solved using conditions: {ret}")
            print(f"Solved using regex:      {ret_r}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
