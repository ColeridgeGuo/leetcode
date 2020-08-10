"""
    Given an integer, write a function to determine if it is a power of two.
"""


class Solution:
    def isPowerOfTwo_iterative(self, n: int) -> bool:
        while n > 1:
            n /= 2
        return n == 1
    
    def isPowerOfTwo_recursive(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return n%2 == 0 and self.isPowerOfTwo_recursive(n // 2)
    
    def isPowerOfTwo_bit(self, n: int) -> bool:
        return not n & n - 1
    
    def isPowerOfTwo_bit_count(self, n: int) -> bool:
        return bin(n).count('1') == 1
        

def main():
    while True:
        try:
            line = input()
            n = int(line)
            
            sol = Solution()
            ret_iter = sol.isPowerOfTwo_iterative(n)
            ret_recur = sol.isPowerOfTwo_recursive(n)
            ret_bit = sol.isPowerOfTwo_bit(n)
            ret_bit_count = sol.isPowerOfTwo_bit_count(n)
            
            print(f"Solved iteratively:                 {ret_iter}")
            print(f"Solved recursively:                 {ret_recur}")
            print(f"Solved with bit operation:          {ret_bit}")
            print(f"Solved with counting number of 1's: {ret_bit_count}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
