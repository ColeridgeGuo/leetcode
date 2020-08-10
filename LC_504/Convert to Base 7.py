"""
Given an integer, return its base 7 string representation.
"""


class Solution:
    def convertToBase7_iterative(self, num: int) -> str:
        res, n = [], abs(num)
        while n:
            n, r = divmod(n, 7)
            res.append(str(r))
        return '-' * (num < 0) + ''.join(res[::-1]) or '0'
    
    def convertToBase7_recursive(self, num: int) -> str:
        if num < 0:
            return f'-{self.convertToBase7_recursive(-num)}'
        if num < 7:
            return str(num)
        return self.convertToBase7_recursive(num // 7) + str(num % 7)


def main():
    while True:
        try:
            line = input()
            num = int(line)

            sol = Solution()
            ret_iter = sol.convertToBase7_iterative(num)
            ret_recur = sol.convertToBase7_recursive(num)
            
            print(f"Solved iteratively: {ret_iter}")
            print(f"Solved recursively: {ret_recur}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
