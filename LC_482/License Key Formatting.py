"""
You are given a license key represented as a string S which consists only
alphanumeric character and dashes. The string is separated into N+1 groups by N
dashes.

Given a number K, we would want to reformat the strings such that each group
contains exactly K characters, except for the first group which could be shorter
than K, but still must contain at least one character. Furthermore, there must
be a dash inserted between two groups and all lowercase letters should be
converted to uppercase.

Given a non-empty string S and a number K, format the string according to the
rules described above.
"""
from common_funcs import stringToString


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        """
            Use a pointer to loop through the license key, skip dashes, append
            each char converted to uppercase, and append a dash for every K char
        """
        i, group = -1, 0
        res = ""
        while i >= -(len(S)):
            if S[i] == '-':
                i -= 1
                continue
            res = S[i].upper() + res
            group += 1
            if group == K:
                res = '-' + res
                group = 0
            i -= 1
        if res.startswith('-'):
            res = res[1:]
        return res
    
    def licenseKeyFormatting_2(self, S: str, K: int) -> str:
        """
            Remove all dashes in S, convert it to uppercase and reverse it. Then
            join every K chars with a dash
        """
        chars = S.replace('-', '').upper()[::-1]
        return '-'.join(chars[i:i+K] for i in range(0, len(chars), K))[::-1]
    
    def licenseKeyFormatting_3(self, S: str, K: int) -> str:
        """
            Loop through S right-to-left and append each char, only append dash
            every K chars
        """
        res = []
        for i in range(len(S) - 1, -1, -1):
            if S[i] != '-':
                if len(res) % (K + 1) == K:
                    res.append('-')
                res.append(S[i])
        return ''.join(res[::-1]).upper()


def main():
    while True:
        try:
            line = input()
            S = stringToString(line)
            line = input()
            K = int(line)

            sol = Solution()
            ret = sol.licenseKeyFormatting(S, K)
            ret_2 = sol.licenseKeyFormatting_2(S, K)
            ret_3 = sol.licenseKeyFormatting_3(S, K)
            
            print(f"Solved using a pointer:                   {ret}")
            print(f"Solved by joining every K chars:          {ret_2}")
            print(f"Solved by appending a dash every K chars: {ret_3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
