"""
Given two strings A and B, find the minimum number of times A has to be repeated
such that B is a substring of it. If no such solution, return -1.
For example, with A = "abcd" and B = "cdabcdab".
Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring
of it; and B is not a substring of A repeated two times ("abcdabcd").
"""
from common_funcs import stringToString


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        """
        Suppose q is the least number for which len(B) <= len(A * q), or the
        least number of times for A to repeat to be longer than A. We only need
        to check whether B is a substring of A * q or A * (q+1). If we try
        k < q, then B has larger length than A * q and therefore can't be a
        substring. When k = q+1, A * k is already big enough to try all
        positions for B
        Time Complexity: O(N*(N+M)), M = len(A), N = len(B)
        Space complexity:
        """
        least_repeat_times = (len(B) - 1) // len(A) + 1  # equivalent to ceil()
        if B in A * least_repeat_times:
            return least_repeat_times
        if B in A * (least_repeat_times+1):
            return least_repeat_times+1
        return -1


def main():
    while True:
        try:
            line = input()
            A = stringToString(line)
            line = input()
            B = stringToString(line)
            
            sol = Solution()
            ret = sol.repeatedStringMatch(A, B)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
