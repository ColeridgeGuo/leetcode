"""
Given an integer (signed 32 bits), write a function to check whether it is a
power of 4.
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num > 1:
            num = num / 4
        return num == 1
    
    def isPowerOfFour_bit(self, num: int) -> bool:
        return num > 0 and (num & (num - 1)) == 0 and (num - 1) % 3 == 0


def main():
    while True:
        try:
            line = input()
            n = int(line)
            
            sol = Solution()
            ret = sol.isPowerOfFour(n)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
