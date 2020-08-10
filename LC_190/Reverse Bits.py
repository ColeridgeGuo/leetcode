"""
    Reverse bits of a given 32 bits unsigned integer.
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{n:032b}"[::-1], 2)


def main():
    while True:
        try:
            line = input()
            n = int(line)
            
            sol = Solution()
            ret = sol.reverseBits(n)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
