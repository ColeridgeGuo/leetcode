"""
Given a linked list, reverse the nodes of a linked list k at a time and return
its modified list.

k is a positive integer and is less than or equal to the length of the linked
list. If the number of nodes is not a multiple of k then left-out nodes in the
end should remain as it is.
"""
from common_funcs import ListNode, stringToListNode, listNodeToString


class Solution:
    def reverseKGroup_iter1(self, head: ListNode, k: int) -> ListNode:
        dummy = prev = ListNode(next=head)
        i = 0
        while head:
            i += 1
            if i % k == 0:
                prev = self.reverse(prev, head.next)
                head = prev.next
            else:
                head = head.next
        return dummy.next

    def reverse(self, start: ListNode, end: ListNode) -> ListNode:
        curr, first, prev = start.next, start.next, start
        while curr != end:
            curr.next, prev, curr = prev, curr, curr.next
        start.next, first.next = prev, curr
        return first
    
    def reverseKGroup_iter2(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(next=head)
        left = right = head
        while True:
            count = 0
            while right and count < k:
                count += 1
                right = right.next
            if count == k:
                prev, curr = right, left
                for _ in range(k):
                    curr.next, prev, curr = prev, curr, curr.next
                jump.next, jump, left = prev, left, right
            else:
                return dummy.next
    
    def reverseKGroup_recur(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        left = right = head  # [left, right) includes k elements to be reversed
        for _ in range(k):
            if not right:  # base case: no reversing when less than k elements
                return head
            right = right.next
        # reverse first k elements
        new_head = self.reverse2(left, right)
        # recursively reverse the rest of the linked list and link them
        left.next = self.reverseKGroup_recur(right, k)
        return new_head
    
    def reverse2(self, a: ListNode, b: ListNode) -> ListNode:
        pre, cur = None, a
        while cur != b:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


def main():
    while True:
        try:
            line = input()
            head = stringToListNode(line)
            head2 = stringToListNode(line)
            head3 = stringToListNode(line)
            line = input()
            k = int(line)
            
            sol = Solution()
            ret_i1 = sol.reverseKGroup_iter1(head, k)
            ret_i2 = sol.reverseKGroup_iter2(head2, k)
            ret_r = sol.reverseKGroup_recur(head3, k)
            
            out_i1 = listNodeToString(ret_i1)
            out_i2 = listNodeToString(ret_i2)
            out_r = listNodeToString(ret_r)
            print(f"Solved iteratively:    {out_i1}")
            print(f"Solved iteratively II: {out_i2}")
            print(f"Solved recursively:    {out_r}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
