"""
You are given a string s, which contains stars *.

In one operation, you can:

- Choose a star in s.
- Remove the closest non-star character to its left, as well as remove the star
itself.

Return the string after all stars have been removed.

Note:

- The input will be generated such that the operation is always possible.
- It can be shown that the resulting string will always be unique.
"""
from common_funcs import stringToString, stringToString_out


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.removeStars(s)

            out = stringToString_out(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
