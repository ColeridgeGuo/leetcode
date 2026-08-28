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

class MinStack2:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(self.min_stack[-1], value))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def main():
    while True:
        try:
            operations = input()
            numbers = input()
            operations = stringToList(operations)
            numbers = stringToList(numbers)
            
            minStack = None
            minStack2 = None
            for i, operation in enumerate(operations):
                if operation == "MinStack":
                    minStack = MinStack()
                    minStack2 = MinStack2()
                elif operation == "push":
                    minStack.push(numbers[i][0])
                    minStack2.push(numbers[i][0])
                elif operation == "pop":
                    minStack.pop()
                    minStack2.pop()
                elif operation == "top":
                    top = minStack.top()
                    top2 = minStack2.top()
                    print(top)
                    print(top2)
                elif operation == "getMin":
                    m = minStack.getMin()
                    m2 = minStack2.getMin()
                    print(m)
                    print(m2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
