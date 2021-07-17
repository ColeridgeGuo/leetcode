"""
Given two integers n and k, return all possible combinations of k numbers out of 
the range [1, n]. You may return the answer in any order.
"""
from typing import List
from common_funcs import listToString


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return list(combinations(range(1, n+1), k))

    def combine_2(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        res = []

        def backtrack(track: List[int], i: int):
            if len(track) == k:
                res.append(track[:])
                return
            for j in range(i, n):
                track.append(nums[j])
                backtrack(track, j+1)
                track.pop()

        backtrack([], 0)
        return res

    def combine_3(self, n: int, k: int) -> List[List[int]]:
        """
        C(n, k) = C(n-1, k-1) + C(n-1, k)
        To choose k from n nums, either n is chosen or n is not
        If n is chosen, choose k-1 from n-1 and add n to every result;
        If n is not chosen, choose k-1 from n
        """
        if k == n or not k:
            return [list(range(1, k+1))]
        res = [x+[n] for x in self.combine_3(n-1, k-1)]  # chose n
        res.extend(self.combine_3(n-1, k))               # didn't choose n
        return res

    def combine_4(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = [0] * k
        i = 0
        while i >= 0:
            temp[i] += 1
            if temp[i] > n:
                i -= 1
            elif i == k - 1:
                res.append(temp[:])
            else:
                i += 1
                temp[i] = temp[i-1]
        return res

    def combine_5(self, n: int, k: int) -> List[List[int]]:
        """
        Start with C(n,1): [[1], [2], ..., [n-1]], in the following iterations, 
        add the next combination one at a time.
        """
        # start with lists of n choose 1
        res = [[x] for x in range(1, n-k+2)]
        # choose more than 1
        for i in range(2, k+1):
            temp = []
            # iterate thru previous results and append new combination
            for l in res:
                # l[-1]+1 to ensure next element is one larger
                # n-k+i is how many remaining combs we still have to add
                for m in range(l[-1]+1, n-k+i+1):
                    temp.append(l + [m])
            res = temp
        return res


def main():
    while True:
        try:
            line = input()
            n = int(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.combine(n, k)
            ret2 = sol.combine_2(n, k)
            ret3 = sol.combine_3(n, k)
            ret4 = sol.combine_4(n, k)
            ret5 = sol.combine_5(n, k)

            out = listToString(ret)
            out2 = listToString(ret2)
            out3 = listToString(ret3)
            out4 = listToString(ret4)
            out5 = listToString(ret5)
            print(f"Solved using itertools' combinations:    {out}")
            print(f"Solved using backtracking:               {out2}")
            print(f"Solved using formula for combinations:   {out3}")
            print(f"Solved iteratively similar to backtrack: {out4}")
            print(f"Solved iteratively:                      {out5}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
