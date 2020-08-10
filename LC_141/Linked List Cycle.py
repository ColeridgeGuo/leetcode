"""
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which
represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.
"""
from common_funcs import ListNode, stringToList


class Solution:
    def hasCycle_hash(self, head: ListNode) -> bool:
        """
            Using hashtable/dictionary to store nodes already seen so that if
            any cycle exists, it can be found in nodesSeen.
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        nodeSeen = set()
        while head:
            if head in nodeSeen:
                return True
            nodeSeen.add(head)
            head = head.next
        return False
    
    def hasCycle_hare_tortoise(self, head: ListNode) -> bool:
        """
            Floyd's Hare and Tortoise Algorithm: two pointers, one moving 1 step
            at a time and one 2 steps at a time. If cycle exists, the fast
            pointer will eventually catch up with the slow pointer; otherwise,
            the fast will reach the end.
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        hare = tortoise = head
        while tortoise and tortoise.next:
            hare = hare.next                # hare takes one step
            tortoise = tortoise.next.next   # tortoise takes two steps
            if hare == tortoise:
                return True
        return False


def stringToListNode(input, pos):
    # Generate list from the input
    numbers = stringToList(input)
    
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    cycleStart = None
    for i, number in enumerate(numbers):
        ptr.next = ListNode(number)
        if i == pos:
            cycleStart = ptr.next
        elif i == len(numbers) - 1:
            ptr.next.next = cycleStart
        ptr = ptr.next
    
    ptr = dummyRoot.next
    return ptr


def main():
    while True:
        try:
            numbers = input()
            pos = int(input())
            head = stringToListNode(numbers, pos)
            
            sol = Solution()
            ret_h = sol.hasCycle_hash(head)
            ret_f = sol.hasCycle_hare_tortoise(head)
            
            print(f"Solved using hashtable:                           {ret_h}")
            print(f"Solved using Floyd's Hare and Tortoise Algorithm: {ret_f}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
