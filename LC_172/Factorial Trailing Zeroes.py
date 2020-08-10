"""
    Given an integer n, return the number of trailing zeroes in n!.
    The algorithm should run in logarithmic time complexity.
"""


class Solution:
    def trailingZeroes_iterative(self, n: int) -> int:
        numzeros = 0
        while n > 0:
            numzeros += n // 5
            n = n // 5
        return numzeros
    
    def trailingZeros_recursive(self, n: int) -> int:
        if n == 0:
            return 0
        return n // 5 + self.trailingZeros_recursive(n // 5)


def main():
    while True:
        try:
            line = input()
            n = int(line)
            
            sol = Solution()
            ret_iter = sol.trailingZeroes_iterative(n)
            ret_recur = sol.trailingZeros_recursive(n)
            
            print(f"Solved iteratively: {ret_iter}")
            print(f"Solved recursively: {ret_recur}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
