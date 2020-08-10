from typing import List
from common_funcs import stringToList


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
        
    def __str__(self):
        return f'Employee {self.id}: {self.importance}'


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        d = {e.id: e for e in employees}
        
        def dfs(eid: int) -> int:
            e = d[eid]
            return e.importance + sum(dfs(eid) for eid in e.subordinates)
        
        return dfs(id)


def listToEmployees(l: list) -> List['Employee']:
    return [Employee(e[0], e[1], e[2]) for e in l]


def main():
    while True:
        try:
            line = input()
            employees = stringToList(line)
            employees = listToEmployees(employees)
            line = input()
            id = int(line)
            
            sol = Solution()
            ret = sol.getImportance(employees, id)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
