"""
Determine if a 9x9 Sudoku board is valid.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row
        for i in range(len(board)):
            row = set()
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] not in row:
                        row.add(board[i][j])
                    else:
                        return False
                    
        # check each column
        for j in range(len(board[0])):
            col = set()
            for i in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] not in col:
                        col.add(board[i][j])
                    else:
                        return False
                    
        # check each square
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                square = set()
                for m in range(3):
                    for n in range(3):
                        if board[i+m][j+n] != '.':
                            if board[i+m][j+n] not in square:
                                square.add(board[i+m][j+n])
                            else:
                                return False
        return True
    
    def isValidSudoku_2(self, board: List[List[str]]) -> bool:
        """
        Add the presence of each num in each row/col/square to a set, return
        false if a duplicate is found, otherwise return true at the end
        """
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num != '.':
                    if f'{num} in row {i}' in seen:
                        return False
                    else:
                        seen.add(f'{num} in row {i}')
                        
                    if f'{num} in col {j}' in seen:
                        return False
                    else:
                        seen.add(f'{num} in col {j}')
                        
                    if f'{num} in square {i//3}-{j//3}' in seen:
                        return False
                    else:
                        seen.add(f'{num} in square {i//3}-{j//3}')
        return True
    
    def isValidSudoku_3(self, board: List[List[str]]) -> bool:
        """
        Similar to method 1 but in a systematic way
        """
        for row in board:
            nums = [i for i in row if i != '.']
            if len(set(nums)) != len(nums):
                return False
        
        for col in zip(*board):
            nums = [i for i in col if i != '.']
            if len(set(nums)) != len(nums):
                return False
        
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                square = [board[i+x][j+y] for x in range(3) for y in range(3)]
                nums = [i for i in square if i != '.']
                if len(set(nums)) != len(nums):
                    return False
        return True
    
    def isValidSudoky_4(self, board: List[List[str]]) -> bool:
        """
        Similar to method 2, instead of using set, count number of presences and
        return false if any presence is more than 2 times
        """
        from collections import Counter
        return 1 == max(Counter(
            x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i//3, j//3, c))
        ).values())

def main():
    while True:
        try:
            line = input()
            board = stringToList(line)
            
            sol = Solution()
            ret = sol.isValidSudoku(board)
            ret2 = sol.isValidSudoku_2(board)
            ret3 = sol.isValidSudoku_3(board)
            ret4 = sol.isValidSudoky_4(board)
            
            print(ret)
            print(ret2)
            print(ret3)
            print(ret4)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
