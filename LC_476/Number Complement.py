"""
    Given a positive integer num, output its complement number. The complement
    strategy is to flip the bits of its binary representation.
"""


class Solution:
    def findComplement(self, num: int) -> int:
        """
            A positive integer XORed with all 1's flips all of it bits, e.g.,
            1001 ^ 1111 = 0110. This method finds the bit length using bin()
        """
        return num ^ ((1 << (len(bin(num)) - 2)) - 1)
    
    def findComplement_2(self, num: int) -> int:
        """
            A positive integer XORed with all 1's flips all of it bits, e.g.,
            1001 ^ 1111 = 0110. This method finds the bit length by counting
            directly.
        """
        bits, temp = 0, num
        while temp:
            bits += 1
            temp >>= 1
        return num ^ (2**bits - 1)

    def findComplement_3(self, num: int) -> int:
        """
            A positive integer XORed with all 1's flips all of it bits, e.g.,
            1001 ^ 1111 = 0110. This method finds the bit length by taking the
            log of the num.
        """
        import math
        return num ^ ((2 << int(math.log(num, 2))) - 1)
    
    def findComplement_4(self, num: int) -> int:
        """
            Flip each digit directly by XORing with a 1 on that bit
        """
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num
    
    def findComplement_5(self, num: int) -> int:
        """
            Flip num first (including the leading zeros) using ~num and then get
            the last L bits by & with 11...1 (L ones), e.g., 10 = 0b00001010,
            ~10 = 0b11110101, ~0b11110101 & 0b00001111 = 00000101.
        """
        return ~num & ((1 << num.bit_length())-1)
    
    def findComplement_6(self, num: int) -> int:
        """
            Spread the highest 1-bit onto all the lower bits. Then xor with that
        """
        mask = num
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return num ^ mask


def main():
    while True:
        try:
            line = input()
            num = int(line)

            sol = Solution()
            ret = sol.findComplement(num)
            ret2 = sol.findComplement_2(num)
            ret3 = sol.findComplement_3(num)
            ret4 = sol.findComplement_4(num)
            ret5 = sol.findComplement_5(num)
            ret6 = sol.findComplement_6(num)
            
            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            out4 = str(ret4)
            out5 = str(ret5)
            out6 = str(ret6)
            print(f"Solved using XOR and bin():                         {out}")
            print(f"Solved using XOR with directly counting bit length: {out2}")
            print(f"Solved using XOR with log to find bit length:       {out3}")
            print(f"Solved by flipping bits directly:                   {out4}")
            print(f"Solved by inverting num and keep the last part:     {out5}")
            print(f"Solved by XORing with a mask:                       {out6}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
