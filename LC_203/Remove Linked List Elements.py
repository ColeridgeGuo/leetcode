"""
    Remove all elements from a linked list of integers that have value val.
"""
from common_funcs import ListNode, stringToListNode, listNodeToString


class Solution:
    def removeElements_iterative(self, head: ListNode, val: int) -> ListNode:
        """
            Create a dummy head before head and loop through the list and keep a
            previous pointer: once a node with val encountered, set prev's next
            to node's next (skipping the node)
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        dummy_root = ListNode(next=head)
        prev = dummy_root
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy_root.next
    
    def removeElements_no_dummy_head(self, head: ListNode,
                                     val: int) -> ListNode:
        pointer = head
        while pointer.next:
            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return head.next if head.val == val else head
    
    def removeElements_recursive(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        head.next = self.removeElements_recursive(head.next, val)
        return head.next if head.val == val else head


def main():
    while True:
        try:
            line = input()
            head = stringToListNode(line)
            head1 = stringToListNode(line)
            head2 = stringToListNode(line)
            line = input()
            val = int(line)
            
            sol = Solution()
            ret_iter = sol.removeElements_iterative(head, val)
            ret_recur = sol.removeElements_recursive(head1, val)
            ret_no_dummy_head = sol.removeElements_no_dummy_head(head2, val)
            
            out_iter = listNodeToString(ret_iter)
            out_recur = listNodeToString(ret_recur)
            out_no_dummy_head = listNodeToString(ret_no_dummy_head)
            print(f"Solved iteratively:        {out_iter}")
            print(f"Solved recursively:        {out_recur}")
            print(f"Solved without dummy head: {out_no_dummy_head}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
