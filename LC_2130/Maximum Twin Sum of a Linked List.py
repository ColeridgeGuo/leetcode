"""
In a linked list of even size n, the ith node (0-indexed) of the linked list is
known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the
twin of node 2. These are the only nodes with twins for n = 4.

The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum
of the linked list.
"""
from common_funcs import ListNode, stringToListNode


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        """
        Reverse the second half to pair up with the first half.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # use slow and fast pointers to find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half to pair up to the first half
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        ans = 0
        # iterate through both halves together to find the max twin sum
        while prev:
            if (s := head.val + prev.val) > ans:
                ans = s
            head, prev = head.next, prev.next
        return ans


def main():
    while True:
        try:
            line = input()
            head = stringToListNode(line)

            sol = Solution()
            ret = sol.pairSum(head)

            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
