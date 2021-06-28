"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing 
x causes the value to go outside the signed 32-bit integer range 
[-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers 
(signed or unsigned).
"""


MAX_VALUE = 2147483647
MIN_VALUE = -2147483648

class Solution:

    def reverse(self, x: int) -> int:
        res = 0
        sign = [1, -1][x < 0]
        while x != 0:
            pop = abs(x) % 10
            x = abs(x) // 10
            if res > MAX_VALUE // 10 or (res == MAX_VALUE // 10 and pop > 7):
                return 0
            if res < MIN_VALUE // 10 or (res == MIN_VALUE // 10 and pop < -8):
                return 0
            res = res * 10 + pop
        return res * sign
    
    def reverse_pythonic(self, x: int) -> int:
        sign = [1, -1][x < 0]
        res = sign * int(str(abs(x))[::-1])
        return res if MIN_VALUE <= res <= MAX_VALUE else 0


def main():
    while True:
        try:
            line = input()
            x = int(line)

            sol = Solution()
            ret = sol.reverse(x)
            ret2 = sol.reverse_pythonic(x)

            out = str(ret)
            out2 = str(ret2)
            print(f"Solved in a stack manner: {out}")
            print(f"Solved in a Pythonic way: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
