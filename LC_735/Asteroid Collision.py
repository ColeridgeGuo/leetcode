"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet,
the smaller one will explode. If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.
"""
from typing import List

from common_funcs import stringToList, listToString


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for asteroid in asteroids:
            # positive asteroid always pushed onto the stack as they never meet
            if asteroid > 0 or not ans:
                ans.append(asteroid)
            else:
                # smaller asteroid explodes if a negative one is larger than it
                while ans and 0 < ans[-1] < -asteroid:
                    ans.pop()
                # if both are the same size, both will explode
                if ans and ans[-1] == -asteroid:
                    ans.pop()
                # two negative asteroids will never meet
                elif not ans or ans[-1] < 0:
                    ans.append(asteroid)
        return ans

    def asteroidCollision_2(self, asteroids: List[int]) -> List[int]:
        ans = []
        for asteroid in asteroids:
            # Only the following conditions are processed:
            # - negative asteroids
            # - empty stack (no asteroid seen so far)
            # - top of stack is positive
            while ans and asteroid < 0 < ans[-1]:
                # if both are the same size, both will explode
                if ans[-1] == -asteroid:
                    ans.pop()
                    break
                # smaller asteroid explodes if a negative one is larger than it
                elif ans[-1] < -asteroid:
                    ans.pop()
                    continue
                # negative asteroid is smaller, it explodes
                else:
                    break
            else:
                # if no asteroid so far, we push onto the stack, or
                # positive asteroids always pushed onto the stack
                ans.append(asteroid)
        return ans


def main():
    while True:
        try:
            line = input()
            asteroids = stringToList(line)

            sol = Solution()
            ret = sol.asteroidCollision(asteroids)
            ret2 = sol.asteroidCollision_2(asteroids)

            out = listToString(ret)
            out2 = listToString(ret2)
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
