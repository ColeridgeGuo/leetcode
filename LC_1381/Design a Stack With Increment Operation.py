"""
Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the
maximum number of elements in the stack or do nothing if the stack reached the
maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the
maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val.
If there are less than k elements in the stack, just increment all the elements
in the stack.
"""
from typing import List
from common_funcs import stringToList


class CustomStack:
    
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []
        self.inc = []
        
    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)
            self.inc.append(0)
            
    def pop(self) -> int:
        if not self.stack:
            return -1
        if len(self.stack) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()
    
    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc))-1] += val


def main():
    while True:
        try:
            operations = input()
            numbers = input()
            operations = stringToList(operations)
            numbers = stringToList(numbers)
            
            custom_stack = None
            for i, op in enumerate(operations):
                if op == 'CustomStack':
                    custom_stack = CustomStack(numbers[i][0])
                elif op == 'push':
                    custom_stack.push(numbers[i][0])
                elif op == 'pop':
                    print(custom_stack.pop())
                elif op == 'increment':
                    custom_stack.increment(*numbers[i])
        except StopIteration:
            break


if __name__ == '__main__':
    main()
