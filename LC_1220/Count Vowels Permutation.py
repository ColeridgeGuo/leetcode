"""
Given an integer n, your task is to count how many strings of length n can be
formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

Examples:
    Input: n = 1
    Output: 5
    Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
    
    Input: n = 2
    Output: 10
    Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io",
    "iu", "oi", "ou" and "ua".
"""


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        A vowel must follow another that it is allowed to follow, e.g., 'a' can
        only follow 'e', 'i', and 'u', etc.
        """
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
            # if starting from the end, we can use the rules directly
            # a, e, i, o, u = e, a + i, a + e + o + u, i + u, a
            # e.g., 'a' precedes 'e', 'e' precedes 'a' and 'i', etc.
        return (a + e + i + o + u) % (10 ** 9 + 7)


def main():
    while True:
        try:
            line = input()
            num = int(line)
            
            sol = Solution()
            ret = sol.countVowelPermutation(num)
            
            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
