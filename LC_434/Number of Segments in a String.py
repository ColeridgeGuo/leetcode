"""
Count the number of segments in a string, where a segment is defined to be a
contiguous sequence of non-space characters.
"""
from common_funcs import stringToString


class Solution:
    def countSegments_split(self, s: str) -> int:
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        return len(s.split())
    
    def countSegments_pointer(self, s: str) -> int:
        """
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        isStart = True  # boolean flag for start of a segment
        segments = 0  # number of segments
        for char in s:
            if char != ' ':  # not a space, check if start
                segments += 1 if isStart else 0  # only increment if start
                isStart = False
            else:
                isStart = True  # next non-space char is a start
        return segments


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret_split = sol.countSegments_split(s)
            ret_pt = sol.countSegments_pointer(s)
            
            print(f"Solved using .split(): {ret_split}")
            print(f"Solved using pointer:  {ret_pt}")
            
        except StopIteration:
            break


if __name__ == '__main__':
    main()
