"""
    A binary watch has 4 LEDs on the top which represent the hours (0-11), and
    the 6 LEDs on the bottom represent the minutes (0-59).
    Given a non-negative integer n which represents the number of LEDs that are
    currently on, return all possible times the watch could represent.
"""
from typing import List


def readBinaryWatch(num: int) -> List[str]:
    return [f"{h}:{m:02}"
            for h in range(12) for m in range(60)
            if (bin(h)+bin(m)).count("1") == num]


def main():
    while True:
        try:
            line = input()
            num = int(line)
            ret = readBinaryWatch(num)
            print(ret)
        except StopIteration:
            break
        

if __name__ == '__main__':
    main()
