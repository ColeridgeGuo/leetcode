"""
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a
sequence of its moves, judge if this robot ends up at (0, 0) after it completes
its moves.
The move sequence is represented by a string, and the character moves[i]
represents its ith move. Valid moves are R (right), L (left), U (up), and D
(down). If the robot returns to the origin after it finishes all of its moves,
return true. Otherwise, return false.
Note: The way that the robot is "facing" is irrelevant. "R" will always make the
robot move to the right once, "L" will always make it move left, etc. Also,
assume that the magnitude of the robot's movement is the same for each move.
"""
from common_funcs import stringToString


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        return x == y == 0
    
    def judgeCircle_count(self, moves: str) -> bool:
        return moves.count('R') == moves.count('L') and \
               moves.count('U') == moves.count('D')

    def judgeCircle_complex(self, moves):
        """
        'RUL'.find(m) returns: 0 for 'R', 1 for 'U',  2 for 'L',  -1 for 'D'
        1j**          returns: 1 for 'R', 1j for 'U', -1 for 'L', -1j for 'D'
        sum will cancel off 'L' and 'R', 'U and 'D' separately.
        """
        return not sum(1j ** 'RUL'.find(m) for m in moves)


def main():
    while True:
        try:
            line = input()
            moves = stringToString(line)
            
            sol = Solution()
            ret = sol.judgeCircle(moves)
            ret_c = sol.judgeCircle_count(moves)
            ret_cn = sol.judgeCircle_complex(moves)
            
            print(f"Solved by simulating moves:    {ret}")
            print(f"Solved by counting each moves: {ret_c}")
            print(f"Solved using complex numbers:  {ret_cn}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
