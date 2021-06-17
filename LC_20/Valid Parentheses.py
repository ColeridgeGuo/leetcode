"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
from common_funcs import stringToString


class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"]": "[", "}": "{", ")": "("}

        for ch in s:
            if ch in pairs:
                # return false if the corresponding left not found
                if not stack or pairs[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)  # push left onto stack
        return not stack


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.isValid(s)

            out = str(ret)
            print(f"Solved using stack: {out}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
