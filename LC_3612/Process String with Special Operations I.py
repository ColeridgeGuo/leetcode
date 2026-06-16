"""
You are given a string s consisting of lowercase English letters and the
special characters: '*', '#', and '%'.

Build a new string result by processing s from left to right:

- A lowercase English letter is appended to result.
- A '*' removes the last character from result, if it exists.
- A '#' duplicates the current result and appends it to itself.
- A '%' reverses the current result.

Return the final string result after processing all characters in s.
"""
from common_funcs import stringToString, stringToString_out


class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for char in s:
            if char == '*':
                if result:
                    result.pop()
            elif char == '#':
                result.extend(result)
            elif char == '%':
                result.reverse()
            else:
                result.append(char)
        return ''.join(result)


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.processStr(s)

            out = stringToString_out(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
