"""
    Given an integer, write an algorithm to convert it to hexadecimal. For
    negative integer, two’s complement method is used.
"""


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        letters = '0123456789abcdef'
        res = ""
        for _ in range(8):
            res = letters[num % 16] + res
            num >>= 4
            if num == 0:
                break
        return res
    
    def toHex_oneline(self, num: int) -> str:
        return ''.join('0123456789abcdef'[(num >> 4 * i) & 15]
                       for i in range(8)
                       )[::-1].lstrip('0') or '0'


def main():
    while True:
        try:
            line = input()
            num = int(line)

            sol = Solution()
            ret = sol.toHex(num)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
