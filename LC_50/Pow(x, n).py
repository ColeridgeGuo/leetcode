"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""


class Solution:
    def myPow_recur(self, x: float, n: int) -> float:
        if n == 0:  # base case: x^0 = 1
            return 1
        if n < 0:  # negative exponent: x^-n = 1/x^n
            return 1 / self.myPow_recur(x, -n)
        half = self.myPow_recur(x, n // 2)
        # odd exponent: x^n = x^(n/2) * x^(n/2) * x
        if n % 2:
            return half * half * x
        return half * half  # even exponent: x^n = x^(n/2) * x^(n/2)
    
    def myPow_iter(self, x: float, n: int) -> float:
        m = abs(n)
        res = 1
        while m:
            if m % 2:
                res *= x
            x *= x
            m >>= 1
        return res if n >= 0 else 1/ res


def main():
    while True:
        try:
            line = input()
            x = float(line)
            line = input()
            n = int(line)

            sol = Solution()
            ret = sol.myPow_recur(x, n)
            ret2 = sol.myPow_iter(x, n)

            out = str(ret)
            out2 = str(ret2)
            print(f"Solved recursively: {out}")
            print(f"Solved iteratively: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
