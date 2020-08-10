"""
    Given a nested list of integers, implement an iterator to flatten it.
    Each element is either an integer, or a list -- whose elements may also be
    integers or other lists.
"""


class NestedInteger:
    """
        This is the interface that allows for creating nested lists.
    """
    def __init__(self, val=None, list=None):
        if list is None:
            list = []
        self.val = val
        self.list = list
        
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a
        nested list.
        """
        return self.val != 0
        
    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a
        single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.val
    
    def getList(self) -> ["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a
        nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.list
       

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = nestedList
    
    def next(self) -> int:
        return self.list.pop().getInteger()
    
    def hasNext(self) -> bool:
        pass


def stringToNestList(s):
    return []


def main():
    while True:
        try:
            line = input()
            
            nestedList = []
            i, v = NestedIterator(nestedList), []
            while i.hasNext():
                v.append(i.next())
        except StopIteration:
            break


if __name__ == '__main__':
    main()
