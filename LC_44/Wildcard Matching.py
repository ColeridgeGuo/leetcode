"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching
with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
"""
from common_funcs import stringToString


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        dp[i][j]: s[:i] matches p[:j]
                = dp[i-1][j-1] if s[i] == p[j] or p[j] == '?'
                = dp[i-1][j] or dp[i][j-1] if p[j] == '*'
                = False otherwise
        """
        # replace multiple consecutive '*'s with one '*'
        real_len, first_star, pattern = 0, True, list(p)
        for i in range(len(pattern)):
            if pattern[i] == '*':
                if first_star:
                    # increment the real length of pattern if curr char is '*'
                    # and is first in its sequence
                    pattern[real_len] = pattern[i]
                    real_len += 1
                    first_star = False
            else:
                # increment the real length of pattern if curr char is not '*'
                pattern[real_len] = pattern[i]
                real_len += 1
                first_star = True
                
        # initialize dp 2d array
        dp = [[False] * (real_len+1) for _ in range(len(s)+1)]
        dp[0][0] = True  # empty pattern matches empty string
        
        if real_len > 0 and pattern[0] == '*':
            dp[0][1] = True  # first char matches iff pattern starts with '*'
            
        for i in range(len(s)):
            for j in range(real_len):
                if s[i] == pattern[j] or pattern[j] == '?':
                    dp[i+1][j+1] = dp[i][j]
                elif pattern[j] == '*':
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]
        return dp[-1][-1]
    
    def isMatch_fsm(self, s: str, p: str) -> bool:
        transfer = {}
        state = 0
        for char in p:
            if char == '*':
                transfer[state, char] = state
            else:
                transfer[state, char] = state + 1
                state += 1
        accept = state
        states = {0}
        for char in s:
            next_states = set()
            for token in (char, '*', '?'):
                for at in states:
                    next_state = transfer.get((at, token))
                    if next_state is not None:
                        next_states.add(next_state)
            states = next_states
        return accept in states


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            p = stringToString(line)
            
            sol = Solution()
            ret = sol.isMatch(s, p)
            ret2 = sol.isMatch_fsm(s, p)
            
            out = str(ret)
            out2 = str(ret2)
            print(f'Solved using DP:  {out}')
            print(f'Solved using FSM: {out2}')
        except StopIteration:
            break


if __name__ == '__main__':
    main()
