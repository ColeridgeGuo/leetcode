"""
    Implement the following operations of a queue using stacks.
    
    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.
"""
from common_funcs import stringToList


class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []
        self.top = None
    
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.q1:
            self.top = x
        self.q1.append(x)
    
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())
        return self.q2.pop()
    
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.q2:
            return self.q2[-1]
        return self.top
    
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.q1 and not self.q2


def main():
    while True:
        try:
            operations = input()
            numbers = input()
            operations = stringToList(operations)
            numbers = stringToList(numbers)
            
            myQueue = None
            for i, operation in enumerate(operations):
                if operation == "MyQueue":
                    myQueue = MyQueue()
                elif operation == "push":
                    myQueue.push(numbers[i][0])
                elif operation == "pop":
                    popped = myQueue.pop()
                    print(f"Popped off {popped}")
                elif operation == "peek":
                    peeked = myQueue.peek()
                    print(f"Peeked: {peeked}")
                elif operation == "empty":
                    empty = myQueue.empty()
                    print(empty)
        except StopIteration:
            break


if __name__ == '__main__':
    main()