"""
You are given a string s consisting only of the characters '0' and '1'.
In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal.
For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
"""
from common_funcs import stringToString


class Solution:
    def minOperations(self, s: str) -> int:
        letters = list(s)
        letters_ = list(s)
        ans = 0
        for i in range(len(letters) - 1):
            if letters[i] == letters[i + 1]:
                letters[i + 1] = "1" if letters[i] == "0" else "0"
                ans += 1

        letters_[0] = "1" if letters_[0] == "0" else "0"
        ans_ = 1
        for i in range(len(letters) - 1):
            if letters_[i] == letters_[i + 1]:
                letters_[i + 1] = "1" if letters_[i] == "0" else "0"
                ans_ += 1
        return min(ans, ans_)

    def minOperations_2(self, s: str) -> int:
        # number of fixes if s starts with 0/1
        start0 = start1 = 0

        for i in range(len(s)):
            if i % 2 == 0:  # even indices are 0 if s starts with 0, 1 otherwise
                if s[i] == "0":  # start1 increments because s[i] should be 1
                    start1 += 1
                else:  # start0 increments because s[i] should be 0
                    start0 += 1
            else:  # odd indices are 1 if s starts with 0, 0 otherwise
                if s[i] == "0":
                    start0 += 1  # start0 increments because s[i] should be 1
                else:
                    start1 += 1  # start1 increments because s[i] should be 0
        return min(start0, start1)

    def minOperations_3(self, s: str) -> int:
        # only mismatched 0's need to be counted because
        # mismatched 1's will just be the complement wrt len(s)
        start0 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "1":
                    start0 += 1
            else:
                if s[i] == "0":
                    start0 += 1
        return min(start0, len(s) - start0)


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.minOperations(s)
            ret2 = sol.minOperations_2(s)
            ret3 = sol.minOperations_3(s)

            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            print(f"Solved by manually modifying the string: {out}")
            print(f"Solved by counting misplaced 0's or 1's: {out2}")
            print(f"Solved by counting misplaced 0's:        {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
