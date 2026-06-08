"""
Given two non-negative integers num1 and num2 represented as string, return
the sum of num1 and num2.
"""
from common_funcs import stringToString, stringToString_out
from collections import deque


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # num1 is always the longer number
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        res = deque()  # queue to store each digit
        carry = 0
        for i in range(len(num1)):
            # if we run out of num2, treat it as adding zeros
            sum_ = int(num1[~i]) + carry
            if i < len(num2):
                sum_ += int(num2[~i])
            carry, digit = divmod(sum_, 10)

            res.appendleft(str(digit))
        if carry:
            res.appendleft(str(carry))
        return ''.join(res)


def main():
    while True:
        try:
            line = input()
            num1 = stringToString(line)
            line = input()
            num2 = stringToString(line)

            sol = Solution()
            ret = sol.addStrings(num1, num2)
            
            out = stringToString_out(ret)
            print(f"Solved by adding each digit up: {out}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
