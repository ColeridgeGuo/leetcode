"""
Given an integer n, return the number of ways you can write n as the sum of 
consecutive positive integers.
"""


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        """
        N can be written as the sum of consecutive positive integers => then N 
        can be written as x + (x+1) + (x+2) + ... + (x+k-1) in k terms. 
        N = (x+(x+k-1))*k/2 = k(2x+k-1)/2 = kx + (k(k-1))/2 => kx = N - k(k-1)/2
        We iterate thru values for k and if N-k(k-1)/2 is a multiple of k, we 
        have found an x to write N in k consecutive integers.
        """
        res, k = 0, 1
        while k * (k-1) // 2 < N:
            if not (N - k * (k-1) // 2) % k:
                res += 1
            k += 1
        return res


def main():
    while True:
        try:
            line = input()
            N = int(line)

            sol = Solution()
            ret = sol.consecutiveNumbersSum(N)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
