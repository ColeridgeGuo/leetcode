"""
Given a positive integer, check whether it has alternating bits: namely, if two
adjacent bits will always have different values.
"""
from common_funcs import stringToString

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        flag = n & 1
        var = n >> 1
        while var > 0:
            if var & 1 == flag:
                return False
            flag = var & 1
            var >>= 1
        return True
    
    def hasAlternatingBits_bin(self, n: int) -> bool:
        bits = bin(n)
        return all(bits[i] != bits[i+1] for i in range(len(bits) - 1))
    
    def hasAlternatingBits_divmod(self, n: int) -> bool:
        n, cur = divmod(n, 2)
        while n:
            if cur == n % 2:
                return False
            n, cur = divmod(n, 2)
        return True
    
    def hasAlternatingBits_trick(self, n):
        s = bin(n)
        return '00' not in s and '11' not in s
    
    def hasAlternatingBits_xor(self, n):
        """
        n =         1 0 1 0 1 0 1 0
        n >> 1      0 1 0 1 0 1 0 1
        n ^ n>>1    1 1 1 1 1 1 1 1
        n           1 1 1 1 1 1 1 1
        n + 1     1 0 0 0 0 0 0 0 0
        n & (n+1)   0 0 0 0 0 0 0 0
        """
        num = n ^ (n >> 1)
        return not (num & (num + 1))


def main():
    while True:
        try:
            line = input()
            n = stringToString(line)
            
            sol = Solution()
            ret = sol.hasAlternatingBits(n)
            ret_b = sol.hasAlternatingBits(n)
            ret_d = sol.hasAlternatingBits_divmod(n)
            ret_t = sol.hasAlternatingBits_trick(n)
            ret_x = sol.hasAlternatingBits_xor(n)
            
            print(f"Solved by shifting bits:               {ret}")
            print(f"Solved by converting to binary string: {ret_b}")
            print(f"Solved using divmod:                   {ret_d}")
            print(f"Solved using a trick:                  {ret_t}")
            print(f"Solved using XOR:                      {ret_x}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
