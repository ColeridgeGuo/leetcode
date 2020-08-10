"""
You're given a matrix represented by a two-dimensional array, and two positive
integers r and c representing the row number and column number of the wanted
reshaped matrix, respectively. The reshaped matrix need to be filled with all
the elements of the original matrix in the same row-traversing order as they
were. If the 'reshape' operation with given parameters is possible and legal,
output the new reshaped matrix; Otherwise, output the original matrix.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def matrixReshape_flatten(self, nums: List[List[int]],
                              r: int, c: int) -> List[List[int]]:
        flattened = [num for sublist in nums for num in sublist]  # flatten nums
        n = len(flattened)
        if r * c != n:  # if parameters not possible or legal
            return nums
        
        res, temp = [], []
        for i in range(1, n + 1):
            temp.append(flattened[i - 1])
            if i % c == 0:
                res.append(temp)
                temp = []
        return res
    
    def matrixReshape_queue(self, nums: List[List[int]],
                            r: int, c: int) -> List[List[int]]:
        if len(nums) == 0 or r * c != len(nums) * len(nums[0]):
            return nums
        from collections import deque
        queue = deque(num for sublist in nums for num in sublist)
        return [[queue.popleft() for _ in range(c)] for _ in range(r)]
    
    def matrixReshape_direct(self, nums: List[List[int]],
                             r: int, c: int) -> List[List[int]]:
        if len(nums) == 0 or r * c != len(nums) * len(nums[0]):
            return nums
        row = col = 0
        res = [[0] * c for _ in range(r)]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                res[row][col] = nums[i][j]
                col += 1
                if col == c:
                    row, col = row + 1, 0
        return res
    
    def matrixReshape_mod(self, nums: List[List[int]],
                          r: int, c: int) -> List[List[int]]:
        if len(nums) == 0 or r * c != len(nums) * len(nums[0]):
            return nums
        count = 0
        res = [[0] * c for _ in range(r)]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                res[count // c][count % c] = nums[i][j]
                count += 1
        return res


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            r = int(line)
            line = input()
            c = int(line)
            
            sol = Solution()
            ret = sol.matrixReshape_flatten(nums, r, c)
            ret_q = sol.matrixReshape_queue(nums, r, c)
            ret_n = sol.matrixReshape_direct(nums, r, c)
            ret_m = sol.matrixReshape_mod(nums, r, c)
            
            print(f"Solved by flattening nums first:  {ret}")
            print(f"Solved using queue:               {ret_q}")
            print(f"Solved without using extra space: {ret_n}")
            print(f"Solved using modulo:              {ret_m}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
