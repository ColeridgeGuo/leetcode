"""
    The Hamming distance between two integers is the number of positions at
    which the corresponding bits are different.
    Given two integers x and y, calculate the Hamming distance.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
            XORing two numbers gives a new number where the corresponding bit is
            1 if the original two bits were different, and 0 if the same. Now
            count the number of 1's in the new number by shifting one bit to the
            right each time.
            Time Complexity: in linear time of the number of bits in xor
            Space Complexity: O(1)
        """
        xor = x ^ y
        hamming = 0
        while xor > 0:
            hamming += xor & 1
            xor >>= 1
        return hamming
    
    def hammingDistance_2(self, x: int, y: int) -> int:
        """
            Solved the same way as the first one but using Brian Kernighan's bit
            counting algorithm to count the number of 1's.
            Time Complexity:
                worst case: in linear time of the number of bits in xor
                average case: in number of 1-bit's in xor
            Space Complexity: O(1)
        """
        hamming = 0
        xor = x ^ y
        while xor:
            hamming += 1
            xor &= xor - 1
        return hamming
    
    def hammingDistance_3(self, x: int, y: int) -> int:
        """
            Time Complexity: Time Complexity: in linear time of the number of bits in xor
            Space Complexity: O(max(log(x), log(y)))
        """
        return bin(x ^ y).count('1')


def main():
    while True:
        try:
            line = input()
            x = int(line)
            line = input()
            y = int(line)

            sol = Solution()
            ret = sol.hammingDistance(x, y)
            ret_2 = sol.hammingDistance_2(x, y)
            ret_3 = sol.hammingDistance_3(x, y)
            
            out = str(ret)
            out_2 = str(ret_2)
            out_3 = str(ret_3)
            print(f"Solved by XORing two numbers and count 1's: {out}")
            print(f"Solved with Brian Kernighan's algorithm:    {out_2}")
            print(f"Solved by counting 1's in string:           {out_3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
