"""
Given a sorted linked list, delete all duplicates such that each element appear
only once.
"""
from common_funcs import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head

        while current is not None and current.next is not None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


if __name__ == "__main__":
    
    # create a linked list
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    newNode = Solution().deleteDuplicates(node1)
    print(newNode)
