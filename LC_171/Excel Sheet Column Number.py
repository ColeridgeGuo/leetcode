"""
Given a column title as appear in an Excel sheet, return its corresponding
column number. For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
"""
from common_funcs import stringToString


class Solution:
    def titleToNumber_iterative(self, s: str) -> int:
        num = 0
        for i in range(len(s)):
            digit = ord(s[-(i+1)]) - 64
            num += digit * (26 ** i)
        return num
    
    def titleToNumber_reduce(self, s: str) -> int:
        from functools import reduce
        return reduce(lambda x, y: x * 26 + y, [ord(c) - 64 for c in s])


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            
            sol = Solution()
            ret_iter = sol.titleToNumber_iterative(s)
            ret_reduce = sol.titleToNumber_reduce(s)
            
            print(f"Solved iteratively:  {ret_iter}")
            print(f"Solved using reduce: {ret_reduce}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()