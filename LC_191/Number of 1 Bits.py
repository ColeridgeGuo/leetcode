"""
Write a function that takes an unsigned integer and return the number of '1'
bits it has (also known as the Hamming weight).
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    
    def hammingWeight_bit(self, n: int) -> int:
        """
        Any number n & n-1 flips the least significant 1 bit to 0.
        """
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
    
    def hammingWeight_bit_2(self, n: int) -> int:
        """
        Any number n & 1 gives the last bit.
        """
        ones = 0
        while n:
            ones += n & 1
            n = n >> 1
        return ones


def main():
    while True:
        try:
            line = input()
            n = int(line)
            
            sol = Solution()
            ret = sol.hammingWeight(n)
            ret_b = sol.hammingWeight_bit(n)
            ret_b2 = sol.hammingWeight_bit_2(n)
            
            print(f"Solved using bin() and count(): {ret}")
            print(f"Solved using bit manipulation:  {ret_b}")
            print(f"Solved using bit manipulation:  {ret_b2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
