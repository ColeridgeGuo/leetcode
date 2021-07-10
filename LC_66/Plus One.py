"""
Given a non-empty array of decimal digits representing a non-negative integer, 
increment one to the integer. The digits are stored such that the most 
significant digit is at the head of the list, and each element in the array 
contains a single digit. You may assume the integer does not contain any leading 
zero, except the number 0 itself.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in str(int(''.join(map(str, digits)))+1)]

    def plusOne_2(self, digits: List[int]) -> List[int]:
        # add one to the least significant digit
        carry, digits[-1] = divmod(digits[-1] + 1, 10)
        # add any carry to more significant digits
        for i in range(1, len(digits)):
            carry, digits[~i] = divmod(digits[~i] + carry, 10)
        # append carry to the front if there is any
        return [carry] + digits if carry else digits

    def plusOne_3(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            # only 9 + 1 produces carry, so if < 9 we just add 1 and return
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0  # if digit = 9 then make it 0
        return [1] + digits  # return digits with the carry added to the front


def main():
    while True:
        try:
            line = input()
            digits = stringToList(line)
            digits2 = stringToList(line)
            digits3 = stringToList(line)

            sol = Solution()
            ret = sol.plusOne(digits)
            ret2 = sol.plusOne_2(digits2)
            ret3 = sol.plusOne_3(digits3)

            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            print(f"Solved by converting to int/str/list: {out}")
            print(f"Solved by calculating carry over:     {out2}")
            print(f"Solved by adding 1 to digits < 9:     {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
