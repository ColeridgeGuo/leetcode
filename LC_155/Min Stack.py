"""
    Design a stack that supports push, pop, top, and retrieving the minimum
    element in constant time.
    
    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
"""
from common_funcs import stringToList


class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minNum = float('inf')
    
    def push(self, x: int) -> None:
        if x <= self.minNum:
            # whenever a new min is pushed, we push the old min onto the stack,
            # which will later be popped off in pop()
            self.stack.append(self.minNum)
            self.minNum = x
        self.stack.append(x)
    
    def pop(self) -> None:
        # if minNum is popped, the old min is re-set to minNUm
        if self.stack.pop() == self.minNum:
            self.minNum = self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return int(self.minNum)


def main():
    while True:
        try:
            operations = input()
            numbers = input()
            operations = stringToList(operations)
            numbers = stringToList(numbers)
            
            minStack = None
            for i, operation in enumerate(operations):
                if operation == "MinStack":
                    minStack = MinStack()
                elif operation == "push":
                    minStack.push(numbers[i][0])
                elif operation == "pop":
                    minStack.pop()
                elif operation == "top":
                    top = minStack.top()
                    print(top)
                elif operation == "getMin":
                    m = minStack.getMin()
                    print(m)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
