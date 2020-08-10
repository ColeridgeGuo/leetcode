"""
Give a string s, count the number of non-empty (contiguous) substrings that have
the same number of 0's and 1's, and all the 0's and all the 1's in these
substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.
"""
from common_funcs import stringToString


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Group s into consecutive 0's and 1's and count their lengths, then the
        number of 0*1* or 1*0* will be the minimum of two consecutive groups
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        count = [1]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count[-1] += 1
            else:
                count.append(1)
        ans = 0
        for i in range(1, len(count)):
            ans += min(count[i-1], count[i])
        return ans
    
    def countBinarySubstrings_itertools(self, s: str) -> int:
        """
        Use groupby() in itertools to achieve the same effect as in the first
        approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        from itertools import groupby
        count = [len(list(v)) for _, v in groupby(s)]
        return sum(min(p) for p in zip(count, count[1:]))
    
    def countBinarySubstrings_one_pass(self, s: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                ans += min(prev, cur)
                prev, cur = cur, 1
        return ans + min(prev, cur)


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            
            sol = Solution()
            ret = sol.countBinarySubstrings(s)
            ret_i = sol.countBinarySubstrings_itertools(s)
            ret_o = sol.countBinarySubstrings_one_pass(s)
            
            print(f"Solved by counting consecutive 0's and 1's: {ret}")
            print(f"Solved by using itertools.groupby():        {ret_i}")
            print(f"Solved by calculating on the fly:           {ret_o}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
