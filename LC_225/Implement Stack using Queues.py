"""
    Implement the following operations of a stack using queues.
    
    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.
    
    Only .append() and .popleft() can be used from deque
"""
from collections import deque
from common_funcs import stringToList


class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())
            
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.popleft()
    
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[0]
    
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.stack)


def main():
    while True:
        try:
            operations = input()
            numbers = input()
            operations = stringToList(operations)
            numbers = stringToList(numbers)
            
            myStack = None
            for i, operation in enumerate(operations):
                if operation == "MyStack":
                    myStack = MyStack()
                elif operation == "push":
                    myStack.push(numbers[i][0])
                elif operation == "pop":
                    popped = myStack.pop()
                    print(f"Popped off {popped}")
                elif operation == "top":
                    top = myStack.top()
                    print(f"The top is: {top}")
                elif operation == "empty":
                    empty = myStack.empty()
                    print(empty)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
