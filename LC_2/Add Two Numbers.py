"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list. You may assume the
two numbers do not contain any leading zero, except the number 0 itself.
"""
from common_funcs import ListNode, stringToListNode, listNodeToString


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode()
        p1, p2, curr = l1, l2, dummy
        while p1 or p2:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            carry, digit = divmod(carry + val1 + val2, 10)
            curr.next = ListNode(val=digit)
            curr = curr.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        curr.next = ListNode(val=carry) if carry else None
        return dummy.next
    
    def addTwoNumbers_recursive(self, l1, l2):
        
        def toInt(node):
            return node.val + 10 * toInt(node.next) if node else 0
        
        def toList(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = toList(n // 10)
            return node
        return toList(toInt(l1) + toInt(l2))


def main():
    while True:
        try:
            line = input()
            l1 = stringToListNode(line)
            line = input()
            l2 = stringToListNode(line)
            
            sol = Solution()
            ret = sol.addTwoNumbers(l1, l2)
            ret_r = sol.addTwoNumbers_recursive(l1, l2)
            
            out = listNodeToString(ret)
            out_r = listNodeToString(ret_r)
            print(f"Solved by adding each digit:               {out}")
            print(f"Solved by summing two numbers recursively: {out_r}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
