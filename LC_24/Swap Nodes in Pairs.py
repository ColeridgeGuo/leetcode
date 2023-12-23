"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be
changed.
"""
from common_funcs import ListNode, stringToListNode, listNodeToString


class Solution:
    def swapPairs_iter(self, head: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        dummy = prev = ListNode(next_node=head)
        curr = head
        while curr and curr.next:
            # NextNode is the next node of Curr.next to be swapped later
            # NewHead is Curr.next that will become the new head after swapping
            next_node, new_head = curr.next.next, curr.next
            # swap Curr and NewHead, link to NextNode and link Prev to NewHead
            new_head.next = curr
            curr.next = next_node
            prev.next = new_head
            # update Curr and Prev pointers
            prev = curr
            curr = next_node
        return dummy.next
    
    def swapPairs_iter_2(self, head: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        Detail explanation for swapping by changing 3 references:
        https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode
        """
        dummy = prev = ListNode(next_node=head)
        while prev.next and prev.next.next:
            # first, second node in a pair (will become second and first)
            first, second = prev.next, prev.next.next
            # change three references to swap
            prev.next, first.next, second.next = second, second.next, first
            prev = first
        return dummy.next
    
    def swapPairs_recur(self, head: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(n/2) = O(n) stack call takes space
        """
        if not head or not head.next:  # base case: less than 2 nodes
            return head
        # NewHead is Curr.next that will become the new head after swapping
        new_head = head.next
        # recursive call to swap the rest of the list
        head.next = self.swapPairs_recur(head.next.next)
        # swap current node (head) and its next node
        new_head.next = head
        return new_head


def main():
    while True:
        try:
            line = input()
            head1 = stringToListNode(line)
            head2 = stringToListNode(line)
            head3 = stringToListNode(line)
            
            sol = Solution()
            ret_i = sol.swapPairs_iter(head1)
            ret_i2 = sol.swapPairs_iter_2(head2)
            ret_r = sol.swapPairs_recur(head3)
            
            out_i = listNodeToString(ret_i)
            out_i2 = listNodeToString(ret_i2)
            out_r = listNodeToString(ret_r)
            print(f"Solved iteratively w/ dummy head:    {out_i}")
            print(f"Solved iteratively w/ dummy head II: {out_i2}")
            print(f"Solved recursively:                  {out_r}")
            
        except StopIteration:
            break


if __name__ == '__main__':
    main()
