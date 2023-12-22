#!/usr/bin/env python
"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
(t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides 
both str1 and str2.
"""
from common_funcs import stringToString, stringToString_out


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Say s1 = m*GCD, s2 = n*GCD and if s1 and s2 have a GCD,
        then s1 + s2 = (m + n) * GCD = s2 + s1.
        And their GCD is the prefix substring of length the gcd of their lengths,
        i.e., s1[:gcd(len(s1), len(s2))]
        """
        from math import gcd
        return str1[:gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ''

    def gcdOfStrings_recur(self, str1: str, str2: str) -> str:
        """
        If two strings have a GCD, then the shorter string of the two is always 
        a prefix substring of the longer one; otherwise a GCD does not exist. We 
        firs check if the shorter one is a prefix substring of the longer one 
        and recursively check the remaining longer string with the shorter one 
        until one of them is empty
        """
        if len(str1) < len(str2):  # make sure str2 is always shorter
            return self.gcdOfStrings_recur(str2, str1)
        if not str2:  # if shorter string is empty, return longer string
            return str1
        if str1.startswith(str2):  # recursive call if prefix substring matches
            return self.gcdOfStrings_recur(str1[len(str2):], str2)
        return ''  # no GCD

    def gcdOfStrings_iter(self, str1: str, str2: str) -> str:
        """
        If two strings have a GCD, then the prefix substring of length the GCD 
        of their lengths is the GCD.
        def gcd(a: int, b: int) -> int:
            return b if a == 0 else gcd(b % a, a)
        """
        from math import gcd
        from re import fullmatch
        prefix = str1[:gcd(len(str1), len(str2))]
        ptn = f'({prefix})+'
        return prefix if fullmatch(ptn, str1) and fullmatch(ptn, str2) else ''


def main():
    while True:
        try:
            line = input()
            str1 = stringToString(line)
            line = input()
            str2 = stringToString(line)

            sol = Solution()
            ret = sol.gcdOfStrings(str1, str2)
            ret2 = sol.gcdOfStrings_recur(str1, str2)
            ret3 = sol.gcdOfStrings_iter(str1, str2)

            out = stringToString_out(ret)
            out2 = stringToString_out(ret2)
            out3 = stringToString_out(ret3)
            print(f"Solved by concatenating of the two:     {out}")
            print(f"Solved by recursively prefix substring: {out2}")
            print(f"Solved by finding GCD of lengths:       {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
