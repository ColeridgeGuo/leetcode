"""
Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.
"""
from common_funcs import stringToString


class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        counter = Counter(s)
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        return -1


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.firstUniqChar(s)

            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
