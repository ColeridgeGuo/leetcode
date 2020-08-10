"""
    You are playing the following Nim Game with your friend: There is a heap of
    stones on the table, each time one of you take turns to remove 1 to 3
    stones. The one who removes the last stone will be the winner. You will take
    the first turn to remove the stones.
    
    Both of you are very clever and have optimal strategies for the game. Write
    a function to determine whether you can win the game given the number of
    stones in the heap.
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        if n < 4:
            return True
        if n == 4:
            return False
        

def main():
    while True:
        try:
            line = input()
            n = int(line)

            sol = Solution()
            ret = sol.canWinNim(n)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
