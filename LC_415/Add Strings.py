"""
Given two non-negative integers num1 and num2 represented as string, return
the sum of num1 and num2.
"""
from common_funcs import stringToString, stringToString_out


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
            Time Complexity: O(l1 + l2 + lg_10(num1+num2))
            Space Complexity: O(lg_10(num1+num2)
        """
        sum = 0
        for i in range(len(num1)):
            sum += (int(num1[i])) * 10**(len(num1) - i - 1)
        for i in range(len(num2)):
            sum += (int(num2[i])) * 10**(len(num2) - i - 1)
        res = "0" if sum == 0 else ""
        while sum > 0:
            res = str(sum % 10) + res
            sum //= 10
        return res
    
    def addStrings_carry(self, num1: str, num2: str) -> str:
        """
            Time Complexity: O(max(l1, l2))
            Space Complexity: O(max(l1, l2))
            l1=len(num1), l2=len(num2)
        """
        res, carry = [], 0
        p1, p2 = len(num1) - 1, len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = int(num1[p1]) if p1 >= 0 else 0
            x2 = int(num2[p2]) if p2 >= 0 else 0
            carry, value = divmod(x1 + x2 + carry, 10)
            res.append(str(value))
            p1, p2 = p1 - 1, p2 - 1
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1])


def main():
    while True:
        try:
            line = input()
            num1 = stringToString(line)
            line = input()
            num2 = stringToString(line)

            sol = Solution()
            ret = sol.addStrings(num1, num2)
            ret_cr = sol.addStrings_carry(num1, num2)
            
            out = stringToString_out(ret)
            out_cr = stringToString_out(ret_cr)
            print(f"Solved by adding digits up and converting to str: {out}")
            print(f"Solved using math (carry and res):                {out_cr}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
