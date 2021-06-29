"""
Given two non-negative integers num1 and num2 represented as strings, return the 
product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to 
integer directly.
"""
from common_funcs import stringToString


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Mimics long multiplication
        """
        res = 0
        for i in range(len(num2)):
            for j in range(len(num1)):
                res += int(num2[~i]) * int(num1[~j]) * 10**(i + j)
        return str(res)


def main():
    while True:
        try:
            line = input()
            num1 = stringToString(line)
            line = input()
            num2 = stringToString(line)

            sol = Solution()
            ret = sol.multiply(num1, num2)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
