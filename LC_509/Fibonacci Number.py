"""
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
    Fibonacci sequence, such that each number is the sum of the two preceding
    ones, starting from 0 and 1.
"""
import numpy as np
from numpy.linalg import matrix_power


class Solution:
    def fib_recursive(self, N: int) -> int:
        """
        Time Complexity: O(2^N)
        Space Complexity: O(N)
        """
        if N <= 1:
            return N
        return self.fib_recursive(N - 1) + self.fib_recursive(N - 2)
    
    def fib_memoization(self, N: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        sequence = [0, 1]
        for i in range(2, N + 1):
            sequence.append(sequence[i-2] + sequence[i-1])
        return sequence[N]
    
    def fib_memoization_2(self, N: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        prev1, prev2 = 0, 1
        for i in range(N):
            prev1, prev2 = prev2, prev1 + prev2
        return prev1
    
    def fib_math(self, N: int) -> int:
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)
    
    def fib_matrix(self, N: int) -> int:
        """
        Time Complexity: O(log(N))
        Space Complexity: O(log(N))
        """
        if N <= 1:
            return N
        A = np.array([[1, 1], [1, 0]])
        # self.matrix_power(A, N-1)
        A = matrix_power(A, N - 1)
        return A[0][0]
    
    # def matrix_power(self, A: list, N: int):
    #     if N <= 1:
    #         return A
    #
    #     self.matrix_power(A, N//2)
    #     self.multiply(A, A)
    #     B = [[1, 1], [1, 0]]
    #
    #     if N%2 != 0:
    #         self.multiply(A, B)
    #
    # def multiply(self, A: list, B: list):
    #     x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    #     y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    #     z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    #     w = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    #
    #     A[0][0] = x
    #     A[0][1] = y
    #     A[1][0] = z
    #     A[1][1] = w


def main():
    while True:
        try:
            line = input()
            N = int(line)

            sol = Solution()
            # ret_r = sol.fib_recursive(N)
            ret_memo = sol.fib_memoization(N)
            ret_memo2 = sol.fib_memoization_2(N)
            ret_math = sol.fib_math(N)
            ret_mtx = sol.fib_matrix(N)
            
            # out_r = str(ret_r)
            out_memo = str(ret_memo)
            out_memo2 = str(ret_memo2)
            out_math = str(ret_math)
            out_mtx = str(ret_mtx)
            
            # print(f"Solved recursively:                          {out_r}")
            print(f"Solved using memoization:                    {out_memo}")
            print(f"Solved by only storing two previous numbers: {out_memo2}")
            print(f"Solved using golden ratio:                   {out_math}")
            print(f"Solved using matrix multiplcation:           {out_mtx}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
