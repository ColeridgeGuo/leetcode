"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def possible(row: int, col: int, n: str) -> bool:
            """
            A helper function for checking if it is possible to put number n at
            (row, col). It checks duplicates in the entire row, column, and the
            3x3 square.
            """
            for i in range(9):
                if board[row][i] == n:  # check duplicates in the row
                    return False
                if board[i][col] == n:  # check duplicates in the column
                    return False
                
            # top-left corner of 3x3 square
            x0, y0 = (col // 3) * 3, (row // 3) * 3
            for i in range(3):  # check duplicates in the 3x3 square
                for j in range(3):
                    if board[y0+i][x0+j] == n:
                        return False
            return True
        
        def solve(ij: int) -> bool:
            """
            Indexing (ij) the 2D matrix as a long 1D array so that each
            recursive call of solve() does not start from (0,0), but instead
            starts from where the caller left off.
            """
            for k in range(ij, 9 * 9):
                i, j = k // 9, k % 9  # convert 1D index to 2D indices
                if board[i][j] == '.':  # if cell empty (for putting a number)
                    for n in range(1, 10):  # try put in 1-9
                        if possible(i, j, f'{n}'):
                            board[i][j] = f'{n}'  # temporarily put the number
                            if solve(i*9+j+1):  # rest of the board all correct
                                return True
                            board[i][j] = '.'  # otherwise cancel this attempt
                    return False  # no number would fit here
            return True  # this step can only be reached if whole board finished
        
        solve(0)  # start from (0,0)
        

def main():
    while True:
        try:
            line = input()
            board = stringToList(line)
            print("Before: ")
            for row in board:
                print('[', end=' ')
                for num in row:
                    print(num, end=' ')
                print(']')
                
            sol = Solution()
            sol.solveSudoku(board)
            
            print("After: ")
            for row in board:
                print('[', end=' ')
                for num in row:
                    print(num, end=' ')
                print(']')
        except StopIteration:
            break


if __name__ == '__main__':
    main()
