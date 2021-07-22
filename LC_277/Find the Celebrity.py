"""
Among a party of n people, there may exist one celebrity, someone who all the 
other n - 1 people know him, but he does not know any of them. Now you want to 
find out who the celebrity is or verify that there is not one.

You are given a helper function bool knows(a, b) which tells you whether A knows 
B. Implement a function int findCelebrity(n). Return the celebrity's label if 
there is a celebrity in the party. If there is no celebrity, return -1.
"""
from typing import List
from common_funcs import stringToList


class Solution:

    def __init__(self, mtx: List[List[int]]) -> None:
        self.adjacency_matrix = mtx

    # The knows API is already defined for you.
    # return a bool, whether a knows b
    def knows(self, a: int, b: int) -> bool:
        return bool(self.adjacency_matrix[a][b])

    def findCelebrity(self, n: int) -> int:
        """
        Given the definition of a celebrity, one who knows someone or is not 
        known by someone cannot be the celebrity. i.e.,
        !celebrity(a) iff knows(a, b) || !knows(b, a) ∀ a, b

        So we can rule out all non-celebrities and determine if the remaining 
        one is celebrity or not.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        candidate = 0

        # rule out non-celebrities
        for other in range(1, n):
            if self.knows(candidate, other):
                candidate = other  # cand cannot be celeb so we try other
            # else keep assuming candidate is the celeb so do nothing

        # determine the remaining candidate is the celeb
        for other in range(n):
            if candidate == other:  # skip candidate himself
                continue
            # if this candidate is not celeb either, return -1
            if not self.knows(other, candidate) or self.knows(candidate, other):
                return -1
        return candidate


def main():
    while True:
        try:
            line = input()
            adjacency_matrix = stringToList(line)

            sol = Solution(adjacency_matrix)
            ret = sol.findCelebrity(len(adjacency_matrix))

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
