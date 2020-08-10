"""
Given a singly linked list, determine if it is a palindrome.
"""
from common_funcs import ListNode, stringToListNode
        
        
class Solution:
    def isPalindrome_length(self, head: ListNode) -> bool:
        """
            Go thru the linked list one time to get its length. Push the first
            half on a stack, then pop each val off of the stack to check match
            with the second half.
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        l = self.linkedListLength(head)
        i = 0
        first_half = []
        while i < l // 2:  # put first half on stack
            first_half.append(head.val)
            i += 1
            head = head.next
        if l % 2:  # skip middle if odd length
            head = head.next
        while head:  # pop second half off of stack
            if first_half.pop() != head.val:
                return False
            head = head.next
        return True
    
    def linkedListLength(self, head: ListNode) -> int:
        l = 0
        while head:
            l += 1
            head = head.next
        return l
    
    def isPalindrome_reverse(self, head: ListNode) -> bool:
        """
            Use a slow and fast pointer to find the middle of the list. Use the
            slow pointer to reverse the second half of the linked list and
            simultaneously move inward to check if two halves match.
            Time Complexity: O(n)
            Space Complexity:
        """
        slow = fast = head
        while fast and fast.next:  # find middle using slow and fast pointers
            fast = fast.next.next
            slow = slow.next
        if fast:  # if length of list is odd, move slow one node forward
            slow = slow.next
        slow = self.reverse(slow)  # reverse the second half
        fast = head  #
        
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True
    
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next_temp = head.next
            head.next = prev
            prev = head
            head = next_temp
        return prev


def main():
    while True:
        try:
            line = input()
            head1 = stringToListNode(line)
            head2 = stringToListNode(line)
            
            sol = Solution()
            ret_len = sol.isPalindrome_length(head1)
            ret_reverse = sol.isPalindrome_reverse(head2)
            
            print(f"Solved with calculating length first: {ret_len}")
            print(f"Solved with reversing second half:    {ret_reverse}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
