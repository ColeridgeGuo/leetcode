"""
Given n and k, return the kth permutation sequence. 
"""
from common_funcs import stringToList, stringToString


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Use itertools to generate all permutations and lazily return the k-th
        """
        from itertools import permutations, islice
        perm = permutations(str(x) for x in range(1, n+1))
        return ''.join(next(islice(perm, k-1, k)))

    def getPermutation_2(self, n: int, k: int) -> str:
        """
        Permutations for n consist of:
        1 + permutation(2, 3, ..., n) => (n-1)! permutations
        2 + permutation(1, 3, ..., n) => (n-1)! permutations
        ...
        n + permutation(1, 2, ..., n-1)  => (n-1)! permutations
        The k-th permutation must be within the possibilities for k/(n-1)! hence 
        we know our first number is k/(n-1)!
        Repeat the steps, adjusting n and k accordingly to get the full sequence
        """
        from math import factorial
        numbers = list(range(1, n+1))
        res = []
        k -= 1
        for i in range(1, n+1):
            index, k = divmod(k, factorial(n-i))
            res.append(str(numbers.pop(index)))
        return ''.join(res)


def main():
    while True:
        try:
            line = input()
            n = int(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.getPermutation(n, k)
            ret2 = sol.getPermutation_2(n, k)

            out = stringToString(ret)
            out2 = stringToString(ret2)
            print(f"Solved using itertools' permutations:     {out}")
            print(f"Solved by generating one digit at a time: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
