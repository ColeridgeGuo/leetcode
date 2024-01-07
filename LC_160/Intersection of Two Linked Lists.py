"""
Write a program to find the node at which the intersection of two singly linked
lists begins.
Notes:
- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function
    returns
- You may assume there are no cycles anywhere in the entire linked structure
- Your code should preferably run in O(n) time and use only O(1) memory.
"""
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
    
    def getIntersectionNode(self, head_a: ListNode,
                            head_b: ListNode) -> ListNode | None:
        """
            create dummy heads for the shorter list to have the same length as
            the longer one, then simultaneously move both pointers to find the
            intersection
            Time Complexity: O(max(2*|A|, 2*|B|)) + O(max(skipA, skipB))
                             = O(max(|A|, |B|)) = O(n)
            Space Complexity: O(abs(|A|-|B|)) = O(max(|A|, |B|)) = O(n)
        """
        length_a = self.getLength(head_a)  # O(|A|)
        length_b = self.getLength(head_b)  # O(|B|)
        if length_a < length_b:
            for _ in range(length_b - length_a):  # O(|B|-|A|)
                dummy = ListNode()
                dummy.next = head_a
                head_a = dummy
        elif length_b < length_a:
            for _ in range(length_a - length_b):  # O(|A|-|B|)
                dummy = ListNode()
                dummy.next = head_b
                head_b = dummy
                
        ptr_a, ptr_b = head_a, head_b
        # O(k), k = # of leading nodes before the intersection/max(skipA, skipB)
        while ptr_a and ptr_b:
            if ptr_a is ptr_b:
                return ptr_a
            ptr_a = ptr_a.next
            ptr_b = ptr_b.next
        return None

    def getIntersectionNode1(self, head_a: ListNode,
                             head_b: ListNode) -> ListNode | None:
        """
            two-passes to ensure 
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        if not head_a or not head_b:
            return None
        
        pa = head_a  # 2 pointers
        pb = head_b
        
        while pa is not pb:
            pa = head_b if not pa else pa.next
            pb = head_a if not pb else pb.next
            
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
