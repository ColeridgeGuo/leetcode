"""
    Reverse a singly linked list.
"""
from typing import Optional
from common_funcs import ListNode, stringToListNode, listNodeToString
        

class Solution:
    def reverseList_iterative(self, head: ListNode) -> Optional[ListNode]:
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        if not head:
            return None
        reverse_head = ListNode(head.val)
        while head and head.next:
            reverse_head = ListNode(head.next.val, reverse_head)
            head = head.next
        return reverse_head
    
    def reverseList_iterative_2(self, head: ListNode) -> Optional[ListNode]:
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
            head3 = stringToListNode(line)
            
            sol = Solution()
            ret_iter = sol.reverseList_iterative(head)
            ret_iter2 = sol.reverseList_iterative_2(head2)
            ret_recur = sol.reverseList_recursive(head3)
            
            out_iter = listNodeToString(ret_iter)
            out_iter2 = listNodeToString(ret_iter2)
            out_recur = listNodeToString(ret_recur)
            print(f"Solved iteratively:   {out_iter}")
            print(f"Solved iteratively 2: {out_iter2}")
            print(f"Solved recursively:   {out_recur}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
