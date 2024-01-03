"""
    Given an array of characters, compress it in-place. The length after
    compression must always be smaller than or equal to the original array.
    Every element of the array should be a character (not int) of length 1.
    After you are done modifying the input array in-place, return the new length
    of the array.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    
    def compress(self, chars: List[str]) -> int:
        """
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        read = write = 0  # READ and WRITE pointer
        count = 0  # count of current char
        while read < len(chars):  # loop until READ reaches end of string
            while read < len(chars) and chars[read] == chars[write]:
                count += 1  # increment count of current char
                read += 1  # move READ to next chars
            if count > 1:  # write count only if count > 1
                for c in str(count):
                    write += 1
                    chars[write] = c  # write each digit of count
            count = 0  # reset count
            write += 1  # move WRITE one char forward
            if read < len(chars):
                # write where READ is (next char) to the current WRITE position
                chars[write] = chars[read]
        return write
    
    def compress_2(self, chars: List[str]) -> int:
        """
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        anchor = write = 0
        for read, c in enumerate(chars):  # read one char at a time
            # if next char is different or READ is at the end
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]  # write char to WRITE
                write += 1  # move WRITE one char forward
                if read > anchor:  # write count only if count of char > 1
                    for digit in str(read - anchor + 1):
                        chars[write] = digit  # write each digit of count
                        write += 1  # move WRITE one char forward
                anchor = read + 1  # set anchor to next char of READ
        return write


def main():
    while True:
        try:
            line = input()
            chars1 = stringToList(line)
            chars2 = stringToList(line)
            
            sol = Solution()
            ret1 = sol.compress(chars1)
            ret2 = sol.compress_2(chars2)

            print("Solved using read and write pointers:")
            print(f"Compressed string: {chars1} of length {ret1}")
            print()
            print("Solved using read and write pointers with anchor:")
            print(f"Compressed string: {chars2} of length {ret2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
