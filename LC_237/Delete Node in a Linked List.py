"""
Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node.
"""
from common_funcs import ListNode, stringToList, listNodeToString


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


def stringToListNode(input, n):
    # Generate list from the input
    numbers = stringToList(input)
    
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    node = None
    for number in numbers:
        curr = ListNode(number)
        if number == n:
            node = curr
        ptr.next = curr
        ptr = ptr.next
        
    ptr = dummyRoot.next
    return ptr, node


def main():
    while True:
        try:
            line = input()
            n = input()
            head, node = stringToListNode(line, int(n))
            
            ret = Solution().deleteNode(node)
            
            out = listNodeToString(head)
            if ret is not None:
                print("Do not return anything, modify node in-place instead.")
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
