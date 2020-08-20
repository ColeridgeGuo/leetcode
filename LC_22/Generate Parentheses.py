"""
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.
"""
from typing import List
from common_funcs import listToString


class Solution:
    def generateParenthesis_backtrack(self, n: int) -> List[str]:
        """
        Time Complexity : O(4^n / sqrt(n))
        Space Complexity : O(4^n / sqrt(n))
        """
        res = []
        
        def backtrack(s: str, l: int, r: int):
            if len(s) == 2 * n:
                res.append(s)
                return
            if l < n:
                backtrack(s + '(', l + 1, r)
            if r < l:
                backtrack(s + ')', l, r + 1)
        
        backtrack('', 0, 0)
        return res
    
    def generateParenthesis_recur(self, n: int) -> List[str]:
        """
        The result f(n) will be to put an extra "()" pair to f(n-1). To produce
        a valid result, we can only put ")" in a way that there will be i pairs
        "()" inside the extra "()" and n-1-i pairs "()" outside the extra pair.
        
        f(0): ""
        f(1): "("f(0)")"
        f(2): "("f(0)")"f(1), "("f(1)")"f(0)
        f(3): "("f(0)")"f(2), "("f(1)")"f(1), "("f(2)")"f(0)
        ...
        f(n) = "("f(0)")"f(n-1) , "("f(1)")"f(n-2) "("f(2)")"f(n-3) ... "("f(i)")"f(n-1-i) ... "(f(n-1)")"f(0)
        """
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis_recur(c):
                for right in self.generateParenthesis_recur(n - 1 - c):
                    ans.append(f'({left}){right}')
        return ans
    
    def generateParenthesis_dp(self, n: int) -> List[str]:
        """
        Same logic as recursive but with dp to reduce complexity
        """
        dp = [[] for _ in range(n + 1)]
        dp[0] = ['']
        for i in range(1, n + 1):
            for j in range(i):
                dp[i].extend(f'({a}){b}' for a in dp[j] for b in dp[i - j - 1])
        return dp[n]


def main():
    while True:
        try:
            line = input()
            n = int(line)
            
            sol = Solution()
            ret_b = sol.generateParenthesis_backtrack(n)
            ret_r = sol.generateParenthesis_recur(n)
            ret_d = sol.generateParenthesis_dp(n)
            
            out_b = listToString(ret_b)
            out_r = listToString(ret_r)
            out_d = listToString(ret_d)
            print(f"Solved using backtracking:   {out_b}")
            print(f"Solved using closure number: {out_r}")
            print(f"Solved usin dp:              {out_d}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
