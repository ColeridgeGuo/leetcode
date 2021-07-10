"""
Given two binary strings a and b, return their sum as a binary string.
"""
from common_funcs import stringToString


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):  # ensure a is always the shorter number
            a, b = b, a
        a, b = [int(x) for x in a], [int(x) for x in b]
        carry = 0
        # add a to b from right to left
        for i in range(len(a)):
            carry, b[~i] = divmod(a[~i] + b[~i] + carry, 2)
        # add carry to the rest of b from right to left
        for i in range(len(a), len(b)):
            carry, b[~i] = divmod(b[~i] + carry, 2)
        # add carry to the front if any
        if carry:
            b = [carry] + b
        return ''.join(map(str, b))

    def addBinary_2(self, a: str, b: str) -> str:
        carry, res = 0, []
        a, b = list(a), list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            carry, bit = divmod(carry, 2)
            res.append(str(bit))
        return ''.join(res[::-1])

    def addBinary_3(self, a: str, b: str) -> str:
        return f"{int(a, base=2) + int(b, base=2):b}"


def main():
    while True:
        try:
            line = input()
            a = stringToString(line)
            line = input()
            b = stringToString(line)

            sol = Solution()
            ret = sol.addBinary(a, b)
            ret2 = sol.addBinary_2(a, b)
            ret3 = sol.addBinary_3(a, b)

            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            print(f"Solved by adding shorter number to longer one: {out}")
            print(f"Solved by adding bit by bit:                   {out2}")
            print(f"Solved by converting to int:                   {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
