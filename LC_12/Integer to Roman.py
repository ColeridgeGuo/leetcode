"""
Given an integer, convert it to a roman numeral. Input is guaranteed to be
within the range from 1 to 3999.
"""
from common_funcs import stringToString_out


class Solution:
    def intToRoman(self, num: int) -> str:
        charmap = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        res = []
        n, r, base = num, 0, 1
        while n > 0:
            n, r = divmod(n, 10)
            if r < 4:
                res.append(charmap[base] * r)
            elif r == 4:
                res.append(charmap[base] + charmap[5*base])
            elif r == 5:
                res.append(charmap[5*base])
            elif r < 9:
                res.append(charmap[5*base] + charmap[base] * (r % 5))
            elif r == 9:
                res.append(charmap[base] + charmap[10*base])
            base *= 10
        return ''.join(res[::-1])


def main():
    while True:
        try:
            line = input()
            num = int(line)
            
            sol = Solution()
            ret = sol.intToRoman(num)
            
            out = stringToString_out(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
