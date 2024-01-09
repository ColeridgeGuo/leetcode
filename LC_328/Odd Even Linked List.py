"""
Given the head of a singly linked list, group all the nodes with odd indices
together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain
as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time
complexity.
"""
from common_funcs import ListNode, stringToListNode, listNodeToString


class Solution:

    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head:
            return
        odd = head  # pointer for odd nodes
        even = head.next  # pointer for even nodes
        dummy = even  # dummy head for even nodes
        while even and even.next:
            # skip the next even node, link current odd to the next odd node
            odd.next = odd.next.next
            # skip the next odd node, link current even to the next even node
            even.next = even.next.next
            # move on to the next odd node
            odd = odd.next
            # move on the next even node
            even = even.next
        # append even nodes to the odd nodes
        odd.next = dummy
        return head


def main():
    while True:
        try:
            line = input()
            head = stringToListNode(line)

            sol = Solution()
            ret = sol.oddEvenList(head)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
