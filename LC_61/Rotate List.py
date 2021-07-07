"""
Given the head of a linked list, rotate the list to the right by k places.
"""
from common_funcs import stringToListNode, ListNode, listNodeToString


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        First find tail and length, then connect tail to head to form a loop and 
        find new tail and head using k to find the the rotated list
        """
        if not head:
            return head
        # find the tail and the length of the list
        tail, length = head, 1
        while tail.next:
            tail, length = tail.next, length + 1
        # connect tail to head to form a loop
        tail.next = head
        # rotating k times is the same as rotating k % length times
        k %= length
        if k:  # if rotating other than 0 times
            for _ in range(length - k):
                tail = tail.next  # find the new tail
        head = tail.next  # new head is tail.next because it's a loop
        tail.next = None  # un-loop the list
        return head


def main():
    while True:
        try:
            line = input()
            head = stringToListNode(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.rotateRight(head, k)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
