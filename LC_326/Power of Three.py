"""
Given an integer, write a function to determine if it is a power of three.
"""


class Solution:
    def isPowerOfThree_iterative(self, n: int) -> bool:
        while n > 1:
            n = n / 3
        return n == 1
    
    def isPowerOfThree_log(self, n: int) -> bool:
        if n < 1:
            return False
        import math
        return (math.log10(n) / math.log10(3)) % 1 == 0


def main():
    while True:
        try:
            line = input()
            n = int(line)
            
            sol = Solution()
            ret_i = sol.isPowerOfThree_iterative(n)
            ret_l = sol.isPowerOfThree_log(n)
            
            print(f"Solved iteratively: {ret_i}")
            print(f"Solved using log:   {ret_l}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
