"""
    Reverse a singly linked list.
"""
from typing import Optional
from common_funcs import ListNode, stringToListNode, listNodeToString
        

class Solution:
    def reverseList_iterative(self, head: ListNode) -> Optional[ListNode]:
        """
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        prev = None
        while head:
            next_temp = head.next
            head.next = prev
            prev = head
            head = next_temp
        return prev
    
    def reverseList_recursive(self, head: ListNode) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        return p


def main():
    while True:
        try:
            line = input()
            head = stringToListNode(line)
            head2 = stringToListNode(line)
            
            sol = Solution()
            ret_iter = sol.reverseList_iterative(head)
            ret_recur = sol.reverseList_recursive(head2)
            
            out_iter = listNodeToString(ret_iter)
            out_recur = listNodeToString(ret_recur)
            print(f"Solved iteratively:   {out_iter}")
            print(f"Solved recursively:   {out_recur}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
