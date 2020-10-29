"""
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.
"""
from typing import List
from common_funcs import stringToString, listToString


class Solution:
    def letterCombinations_product(self, digits: str) -> List[str]:
        if not digits:
            return []
        from itertools import product
        mapping = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs',
                   8: 'tuv', 9: 'wxyz'}
        return [''.join(tup) for tup in
                product(*(mapping[int(d)] for d in digits))]
    
    def letterCombinations_recursive(self, digits: str) -> List[str]:
        mapping = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs',
                   8: 'tuv', 9: 'wxyz'}
        
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
            else:
                for c in mapping[int(next_digits[0])]:
                    backtrack(combination + c, next_digits[1:])
                    
        res = []
        if digits:
            backtrack("", digits)
        return res
    
    def letterCombinations_BFS(self, digits: str) -> List[str]:
        if not digits:
            return []
        from collections import deque
        res = deque([''])
        mapping = [0, 1, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        for i, d in enumerate(digits):
            while len(res[0]) == i:
                t = res.popleft()
                for s in mapping[int(d)]:
                    res.append(t + s)
        return list(res)
    
    def letterCombinations_reduce(self, digits: str) -> List[str]:
        from functools import reduce
        if not digits:
            return []
        mapping = [0, 1, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        return reduce(lambda acc, d: [x + y for x in acc for y in mapping[int(d)]],
                      digits, [''])


def main():
    while True:
        try:
            line = input()
            digits = stringToString(line)
            
            sol = Solution()
            ret = sol.letterCombinations_product(digits)
            ret_r = sol.letterCombinations_recursive(digits)
            ret_b = sol.letterCombinations_BFS(digits)
            ret_rd = sol.letterCombinations_reduce(digits)
            
            out = listToString(ret)
            out_r = listToString(ret_r)
            out_b = listToString(ret_b)
            out_rd = listToString(ret_rd)
            print(f"Solved using itertools' product: {out}")
            print(f"Solved recursively:              {out_r}")
            print(f"Solved using BFS:                {out_b}")
            print(f"Solved using reduce:             {out_rd}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
