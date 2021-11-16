"""
Given the head of a linked list and a value x, partition it such that all nodes 
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two 
partitions.
"""
from typing import Optional

from common_funcs import ListNode, listNodeToString, stringToListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Keep track of nodes smaller and greater than x while iterating thru the 
        list, appending greater list to smaller list, preserving relative order
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # dummy heads for smaller and greater list
        smaller_head, greater_head = ListNode(), ListNode()
        # pointers keeping track of smaller and greater values
        smaller, greater = smaller_head, greater_head
        while head:
            # update smaller/greater list for each node
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

        greater.next = None  # end the greater list
        smaller.next = greater_head.next  # append greater to smaller
        return smaller_head.next


def main():
    while True:
        try:
            line = input()
            head = stringToListNode(line)
            line = input()
            x = int(line)

            sol = Solution()
            ret = sol.partition(head, x)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
