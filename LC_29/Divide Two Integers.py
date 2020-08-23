"""
Given two integers dividend and divisor, divide two integers without using
multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its
fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        multiply divisor by 2 until the largest multiple smaller than dividend
        found, repeat the process and sum the number of left shifts.
        
        Suppose dividend = 15 and divisor = 3, 15 - 3 > 0. We now try to
        subtract more by shifting 3 to the left by 2 bits (12). Now 15 - 12 > 0,
        shift 12 again to 24, which is larger than 15. So we can at most
        subtract 12 from 15. Since 12 is obtained by shifting 3 to left twice,
        it is 1 << 2 = 4 times of 3. We add 4 to an answer variable (initialized
        to be 0). The above process is like 15 = 3 * 4 + 3. We now get part of
        the quotient (4), with a remaining dividend 3.
        Then we repeat the above process by subtracting divisor = 3 from the
        remaining dividend = 3 and obtain 0. We are done. In this case, no shift
        happens. We simply add 1 << 0 = 1 to the answer variable.
        """
        if dividend == -1 << 31 and divisor == -1:  # the only case of overflow
            return (1 << 31) - 1
        same_sign = (dividend > 0) ^ (divisor > 0)
        dividend, divisor, quotient = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            temp, m = divisor, 1
            while temp << 1 <= dividend:
                temp <<= 1
                m <<= 1
            
            dividend -= temp
            quotient += m
        return -quotient if same_sign else quotient
    
    def divide_2(self, dividend: int, divisor: int) -> int:
        """
        Similar to approach 1, find the largest multiple of divisor smaller than
        dividend by tyring all possible left shifts from 31 to 0.
        """
        if dividend == -1 << 31 and divisor == -1:
            return 2147483647
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        for m in range(32)[::-1]:
            if dividend >> m >= divisor:
                res += 1 << m
                dividend -= divisor << m
        return res if (dividend > 0) == (divisor > 0) else -res


def main():
    while True:
        try:
            line = input()
            dividend = int(line)
            line = input()
            divisor = int(line)
            
            sol = Solution()
            ret = sol.divide(dividend, divisor)
            ret2 = sol.divide_2(dividend, divisor)
            
            out = int(ret)
            out2 = int(ret2)
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
