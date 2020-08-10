"""
Given a non-empty string check if it can be constructed by taking a substring of
it and appending multiple copies of the substring together. You may assume the
given string consists of lowercase English letters only and its length will not
exceed 10000.
"""
from common_funcs import stringToString


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        The maximum length of a repeated substring would be half it's length,
        e.g., S = KK. So SS = KKKK, we will have at least 4 parts of the
        "repeated substring" in ss. If we remove the first and last char of ss,
        the first and last K will be broken up, but we still have remaining K's
        concatenated to form new S's.
        """
        return s in (s + s)[1:-1]
    
    def repeatedSubstringPattern_2(self, s: str) -> bool:
        """
        Find all possible substring lengths (must be factors of len(s) and at
        most len(s)/2), repeat the substring of each length to see if it matches s.
        """
        l = len(s)
        for i in range(1, l // 2 + 1):
            if l % i == 0:
                subS = s[:i]
                j = 1
                while j < l // i:
                    if subS != s[j * i: i + j * i]:
                        break
                    j += 1
                if j == l // i:
                    return True
        return False
    
    def repeatedSubstringPattern_KMP(self, s: str) -> bool:
        i, j, n = 0, 1, len(s)
        pmt = [0] * n + [0]
        while j < n:
            if s[i] == s[j]:
                i, j = i + 1, j + 1
                pmt[j] = i
            elif i == 0:
                j += 1
            else:
                i = pmt[i]
        return pmt[n] != 0 and pmt[n] % (n - pmt[n]) == 0
    
    def repeatedSubstringPattern_regex(self, s: str) -> bool:
        import re
        return bool(re.match(r'(.+)\1+', s))


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.repeatedSubstringPattern(s)
            ret_2 = sol.repeatedSubstringPattern_2(s)
            ret_kmp = sol.repeatedSubstringPattern_KMP(s)
            ret_re = sol.repeatedSubstringPattern_regex(s)
            
            out = str(ret)
            out_2 = str(ret_2)
            out_kmp = str(ret_kmp)
            out_re = str(ret_re)
            print(f"Solved by appending the same string to itself: {out}")
            print(f"Solved by trying all possible substrings:      {out_2}")
            print(f"Solved using KMP's partial match table:        {out_kmp}")
            print(f"Solved using regex:                            {out_re}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
