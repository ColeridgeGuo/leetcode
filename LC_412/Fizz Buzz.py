"""
    Write a program that outputs the string representation of numbers from 1 to
    n. For multiples of three it should output “Fizz” instead of the number and
    for the multiples of five output “Buzz”. For numbers which are multiples of
    both three and five output “FizzBuzz”.
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            fizzbuzz = ""
            if i % 3 == 0:
                fizzbuzz += "Fizz"
            if i % 5 == 0:
                fizzbuzz += "Buzz"
            if not fizzbuzz:
                fizzbuzz += str(i)
            res.append(fizzbuzz)
        return res
    
    def fizzBuzz_oneline(self, n: int) -> List[str]:
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in
                range(1, n + 1)]
    
    def fizzBuzz_no_modulo(self, n: int) -> List[str]:
        res, fizz, buzz = [], 0, 0
        for i in range(1, n+1):
            fizz, buzz = fizz + 1, buzz + 1
            if fizz == 3 and buzz == 5:
                res.append("FizzBuzz")
                fizz, buzz = 0, 0
            elif fizz == 3:
                res.append("Fizz")
                fizz = 0
            elif buzz == 5:
                res.append("Buzz")
                buzz = 0
            else:
                res.append(str(i))
        return res


def main():
    while True:
        try:
            line = input()
            n = int(line)
            
            sol = Solution()
            ret = sol.fizzBuzz(n)
            ret_ol = sol.fizzBuzz_oneline(n)
            ret_nm = sol.fizzBuzz_no_modulo(n)
            
            print(f"Solved with modulo: {ret}")
            print(f"Solved in one line: {ret_ol}")
            print(f"Solved w/o modulo:  {ret_nm}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
