"""
    Count the number of prime numbers less than a non-negative number, n.
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        """
            Using the Sieve of Eratosthenes to find all prime numbers up to n.
            Time Complexity: O(n * log( log (n) ))
            Space Complexity: O(n)
        """
        is_prime = [1]*n  # whether each integer up to n is prime (1) or not (0)
        for i in range(2, int(n**0.5)+1): # start with 2 and check up to sqrt(n)
            if not is_prime[i]:  # if not prime, skip checking its multiples
                continue
            for j in range(i*i, n, i):  # start with i^2,
                is_prime[j] = 0  # mark multiples of the number as not prime (0)
        return is_prime[2:].count(1)  # skip 0 and 1, and count # of 1's


def main():
    while True:
        try:
            line = input()
            n = int(line)
            
            ret = Solution().countPrimes(n)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
