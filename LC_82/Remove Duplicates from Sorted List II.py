"""
Given the head of a sorted linked list, delete all nodes that have duplicate 
numbers, leaving only distinct numbers from the original list. 
Return the linked list sorted as well.
"""
from common_funcs import stringToListNode, ListNode, listNodeToString


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(next_node=head)  # dummy head before original head
        # fast points to the last node w/i a group of identical numbers
        # slow points to the node before each group of identical numbers
        fast, slow = head, dummy

        while fast:
            # move fast all the way to the last node of a duplication group
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            # slow's next node being fast means there's no duplication
            if slow.next == fast:
                slow, fast = slow.next, fast.next
            # slow's next node not being fast means there's duplication so set
            # slow's next to fast's next so that all duplicates are removed
            else:
                slow.next = fast = fast.next
        return dummy.next

    def deleteDuplicates_2(self, head: ListNode) -> ListNode:
        dummy = ListNode(next_node=head)  # dummy head before original head
        # fast points to the last node w/i a group of identical numbers
        # slow points to the node before each group of identical numbers
        fast, slow = head, dummy

        while fast:
            # there's duplication
            if fast.next and fast.val == fast.next.val:
                # move fast all the way to the last node of the duplication
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                # remove duplicates by setting next of fast to next of slow
                slow.next = fast.next
            # there's no duplication
            else:
                # simply move slow forward
                slow = slow.next
            # move fast forward either way
            fast = fast.next
        return dummy.next


def main():
    while True:
        try:
            line = input()
            head = stringToListNode(line)
            head2 = stringToListNode(line)

            sol = Solution()
            ret = sol.deleteDuplicates(head)
            ret2 = sol.deleteDuplicates_2(head2)

            out = listNodeToString(ret)
            out2 = listNodeToString(ret2)
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
