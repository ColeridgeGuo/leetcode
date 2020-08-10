"""
We define the Perfect Number is a positive integer that is equal to the sum of
all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect
number and false when it is not.
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        Time Limit Exceeded
        """
        if num <= 0:
            return False
        return num == sum(i for i in range(1, num) if num % i == 0)

    def checkPerfectNumber_2(self, num: int) -> bool:
        """
        Time complexity : O(sqrt(n))
        Space complexity : O(1)
        """
        if num <= 0:
            return False
        sqrt = int(num**.5)
        divisor_sum = sum(i + num // i for i in range(1, sqrt+1) if not num % i)
        if num == sqrt**2:
            divisor_sum -= sqrt
        return num == divisor_sum - num
    
    def pn(self, p: int) -> int:
        return (1 << (p - 1)) * ((1 << p) - 1)
    
    def checkPerfectNumber_3(self, num: int) -> bool:
        """
        Euclid proved that 2^(p-1)*(2^p - 1) is an even perfect number whenever
        2^p − 1 is prime, where p is prime.
        Time complexity: O(log(n))
        Space complexity: O(log(n))
        """
        primes = [2,3,5,7,13,17,19,31]
        for prime in primes:
            if self.pn(prime) == num:
                return True
        return False


def main():
    while True:
        try:
            line = input()
            num = int(line)

            sol = Solution()
            ret = sol.checkPerfectNumber(num)
            ret2 = sol.checkPerfectNumber_2(num)
            ret3 = sol.checkPerfectNumber_3(num)
            
            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            print(out)
            print(out2)
            print(out3)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
