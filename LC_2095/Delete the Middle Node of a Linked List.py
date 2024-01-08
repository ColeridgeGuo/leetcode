"""
You are given the head of a linked list. Delete the middle node, and return the
head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start
using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal
to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""
from common_funcs import stringToListNode, ListNode, listNodeToString


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        length = 0
        curr = head
        # iterating through the list to get its length
        while curr:
            length += 1
            curr = curr.next
        if length <= 1:
            return
        curr = head
        length //= 2

        # go the node before the middle one
        while length > 1:
            curr = curr.next
            length -= 1
        # remove the middle node
        curr.next = curr.next.next
        return head

    def deleteMiddle_2(self, head: ListNode | None) -> ListNode | None:
        dummy = fast = slow = ListNode(next_node=head)
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return dummy.next


def main():
    while True:
        try:
            line = input()
            head = stringToListNode(line)
            head2 = stringToListNode(line)

            sol = Solution()
            ret = sol.deleteMiddle(head)
            ret2 = sol.deleteMiddle_2(head2)

            out = listNodeToString(ret)
            out2 = listNodeToString(ret2)
            print(f"Solved by calculating length:    {out}")
            print(f"Solved by slow and fast pointer: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
