"""
Given the head of a sorted linked list, delete all duplicates such that each 
element appears only once. Return the linked list sorted as well.
"""
from common_funcs import stringToListNode, ListNode, listNodeToString


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


def main():
    while True:
        try:
            line = input()
            head = stringToListNode(line)

            sol = Solution()
            ret = sol.deleteDuplicates(head)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
