"""
Suppose you have a long flowerbed in which some of the plots are planted and
some are not. However, flowers cannot be planted in adjacent plots - they would
compete for water and both would die.
Given a flowerbed (represented as an array containing 0 and 1, where 0 means
empty and 1 means not empty), and a number n, return if n new flowers can be
planted in it without violating the no-adjacent-flowers rule.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, planted in enumerate(flowerbed):
            if not planted:
                if i == 0 or not flowerbed[i - 1]:
                    if i == len(flowerbed) - 1 or not flowerbed[i + 1]:
                        flowerbed[i] = 1
                        n -= 1
        return n <= 0


def main():
    while True:
        try:
            line = input()
            flowerbed = stringToList(line)
            line = input()
            n = int(line)

            sol = Solution()
            ret = sol.canPlaceFlowers(flowerbed, n)

            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
