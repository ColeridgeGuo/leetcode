"""
You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in
    this round.
"+" (one round's score): Represents that the points you get in this round are
    the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are
    the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid
    round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before
and the round after.
You need to return the sum of the points you could get in all the rounds.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        """
        Use a stack to keep track of previous valid rounds' points. Push every
        valid round's score and pop invalid round's score.
        """
        res, stack = 0, []
        for op in ops:
            if op == 'C':
                res -= stack.pop()
            elif op == 'D':
                res += 2 * stack[-1]
                stack.append(2 * stack[-1])
            elif op == '+':
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            else:
                res += int(op)
                stack.append(int(op))
        return res
    
    def calPoints_2(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)


def main():
    while True:
        try:
            line = input()
            ops = stringToList(line)
            
            sol = Solution()
            ret = sol.calPoints(ops)
            ret_2 = sol.calPoints_2(ops)
            
            print(f"Solved with stack and calculate sum at every move: {ret}")
            print(f"Solved with stack and calculate sum at the end:    {ret_2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
