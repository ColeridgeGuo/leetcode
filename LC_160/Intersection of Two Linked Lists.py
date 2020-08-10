"""
Write a program to find the node at which the intersection of two singly linked
lists begins.
Notes:
- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function returns
- You may assume there are no cycles anywhere in the entire linked structure
- Your code should preferably run in O(n) time and use only O(1) memory.
"""
from typing import Optional
from common_funcs import ListNode, listNodeToString


class Solution:
    def getLength(self, head: ListNode) -> int:
        """
            non-destructively calculate the length of list
        """
        ptr = head
        length = 0
        while ptr:
            length += 1
            ptr = ptr.next
        return length
        
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
            create dummy heads for the shorter list to have the same length as
            the longer one, then simultaneously move both pointers to find the
            intersection
            Time Complexity: O(max(2*|A|, 2*|B|)) + O(max(skipA, skipB))
                             = O(max(|A|, |B|)) = O(n)
            Space Complexity: O(abs(|A|-|B|)) = O(max(|A|, |B|)) = O(n)
        """
        lengthA = self.getLength(headA)  # O(|A|)
        lengthB = self.getLength(headB)  # O(|B|)
        if lengthA < lengthB:
            for _ in range(lengthB - lengthA):  # O(|B|-|A|)
                dummy = ListNode(None)
                dummy.next = headA
                headA = dummy
        elif lengthB < lengthA:
            for _ in range(lengthA - lengthB):  # O(|A|-|B|)
                dummy = ListNode(None)
                dummy.next = headB
                headB = dummy
        
        ptrA, ptrB = headA, headB
        # O(k), k = # of leading nodes before the intersection/max(skipA, skipB)
        while ptrA and ptrB:
            if ptrA is ptrB:
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next
        return None

    def getIntersectionNode1(self, headA, headB) -> Optional[ListNode]:
        """
            two-passes to ensure 
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        if not headA or not headB:
            return None
    
        pa = headA  # 2 pointers
        pb = headB
    
        while pa is not pb:
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next
    
        return pa


def main():
    node1 = ListNode(4)
    node2 = ListNode(1)
    node3 = ListNode(8)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(5)
    node7 = ListNode(0)
    node8 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node6.next = node7
    node7.next = node8
    node8.next = node3
    
    ret = Solution().getIntersectionNode1(node1, node6)
    
    out = listNodeToString(ret)
    print(out)


if __name__ == '__main__':
    main()
