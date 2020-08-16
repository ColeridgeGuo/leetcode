"""
Given a linked list, remove the n-th node from the end of list and return its
head.
"""
from common_funcs import ListNode, stringToListNode, listNodeToString


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Time Complexity: O(2n) = O(n)
        Space Complexity: O(1)
        """
        length, curr = 0, head
        while curr:
            length, curr = length + 1, curr.next
        if n == length:  # if head removed
            return head.next
        pointer, curr = 0, head
        while curr:
            if pointer == length - n - 1:
                curr.next = curr.next.next
                break
            pointer, curr = pointer + 1, curr.next
        return head
    
    def removeNthFromEnd_2(self, head: ListNode, n: int) -> ListNode:
        """
        Time Complexity: O(2n) = O(n)
        Space Complexity: O(1)
        """
        dummy = ListNode(next=head)
        length, curr = 0, head
        while curr:
            length, curr = length + 1, curr.next
        length -= n
        curr = dummy
        while length > 0:
            length -= 1
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next

    def removeNthFromEnd_one_pass(self, head: ListNode, n: int) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        dummy = ListNode(next=head)
        pt1 = pt2 = dummy
        for _ in range(n+1):
            pt1 = pt1.next
        while pt1:
            pt1, pt2 = pt1.next, pt2.next
        pt2.next = pt2.next.next
        return dummy.next


def main():
    while True:
        try:
            line = input()
            head = stringToListNode(line)
            head2 = stringToListNode(line)
            head3 = stringToListNode(line)
            line = input()
            n = int(line)
            
            sol = Solution()
            ret = sol.removeNthFromEnd(head, n)
            ret2 = sol.removeNthFromEnd_2(head2, n)
            ret3 = sol.removeNthFromEnd_one_pass(head3, n)
            
            out = listNodeToString(ret)
            out2 = listNodeToString(ret2)
            out3 = listNodeToString(ret3)
            print(f"Solved by counting length in 2 passes:    {out}")
            print(f"Solved by counting length in 2 passes II: {out2}")
            print(f"Solved by using two pointers in 1 pass:   {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
