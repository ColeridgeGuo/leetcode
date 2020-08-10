"""
Given a non-negative integer c, your task is to decide whether there're two
integers a and b such that a^2 + b^2 = c.
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Time complexity : O(sqrt(c)*log(c))
        Space complexity : O(1)
        """
        for i in range(int(c**.5)+1):
            sq = c - i**2
            if sq**.5 == int(sq**.5):
                return True
        return False
    
    def judgeSquareSum_binary_search(self, c: int) -> bool:
        """
        Time complexity : O(sqrt(c)*log(c))
        Space complexity : O(log(c))
        """
        def binary_search(lo, hi, n):
            if lo > hi:
                return False
            mid = lo + (hi - lo) // 2
            if mid**2 == n:
                return True
            if mid**2 > n:
                return binary_search(lo, mid-1, n)
            return binary_search(mid+1, hi, n)
        
        for i in range(int(c**.5)+1):
            sq = c - i**2
            if binary_search(0, sq, sq):
                return True
        return False

    def judgeSquareSum_feramt(self, c: int) -> bool:
        """
        Any positive number nn is expressible as a sum of two squares iff in the
        prime factorization of n, every prime of the form (4k+3) occurs an even
        number of times.
        Time complexity : O(sqrt(c)*log(c))
        Space complexity : O(1)
        """
        for i in range(2, int(c**.5)+1):
            count = 0  # number of the current prime factors
            if c % i == 0:  # if a prime factor is found
                while c % i == 0:  # prime factor remains the same
                    count += 1
                    c //= i
                if i % 4 == 3 and count % 2:
                    # the prime factor appears odd number of times
                    return False
        return c % 4 != 3  # if the last prime factor is in form 4k+3


def main():
    while True:
        try:
            line = input()
            c = int(line)

            sol = Solution()
            ret_1 = sol.judgeSquareSum(c)
            ret_bs = sol.judgeSquareSum_binary_search(c)
            ret_fm = sol.judgeSquareSum_feramt(c)
            
            print(f"Solved by checking each # from 0 to sqrt(c):  {ret_1}")
            print(f"Solved by checking each # with binary search: {ret_bs}")
            print(f"Solved using the Fermat's Theorem:            {ret_fm}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
