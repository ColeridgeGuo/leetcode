"""
Given an array of linked-lists lists, each linked list is sorted in ascending
order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
from typing import List, Tuple
from common_funcs import ListNode, stringToList, stringToListNode, listNodeToString
import heapq


class Solution:
    def mergeKLists_compare(self, lists: List[ListNode]) -> ListNode:
        """
        Scan the current heads for the minimum, append it, and advance its list.
        Reuse nodes and update the input list's head pointers.
        k = number of linked lists, N = total number of nodes.
        Time Complexity: O(k * (N + 1)), including the final empty-head scan
        Space Complexity: O(1) auxiliary space
        """
        
        def compare_nodes(nodes: List[ListNode]) -> Tuple[ListNode, int]:
            min_node, min_index = ListNode(val=float('inf')), 0
            for i, node in enumerate(nodes):
                if node and node.val < min_node.val:
                    min_node, min_index = node, i
            return min_node, min_index
        
        dummy = curr = ListNode()
        while any(node for node in lists):
            min_node, list_index = compare_nodes(lists)  # find min node and its index
            curr.next = min_node  # append the selected node to the result
            lists[list_index] = lists[list_index].next  # advance the selected list's head
            curr = curr.next  # move curr pointer to next
        return dummy.next

    def mergeKLists_heapq(self, lists: List[ListNode]) -> ListNode:
        """
        Keep one current head per nonempty list in a min-heap. Pop the minimum
        and replace it with its successor, reusing the original nodes.
        k = number of linked lists, N = total number of nodes.
        Time Complexity: O(k + N * log(k + 1)), including initialization
        Space Complexity: O(k) auxiliary space
        """
        # push all head nodes onto a heap
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        
        dummy = curr = ListNode()
        while heap:
            # Pop the tuple with the smallest value. Unique list indices break
            # ties without comparing nodes; each list has at most one entry.
            val, i, node = heapq.heappop(heap)
            curr.next = node  # append the selected node to the result
            curr = curr.next  # move curr pointer to next
            if node.next:  # push next if node has next node (not last one)
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
    
    def mergeKLists_pq(self, lists: List[ListNode]) -> ListNode:
        """
        Use a priority queue of current heads, ordered by node value. Append
        each minimum and enqueue its successor, reusing the original nodes.
        k = number of linked lists, N = total number of nodes.
        Time Complexity: O(k + N * log(k + 1)), including initialization
        Space Complexity: O(k) auxiliary space
        """
        from queue import PriorityQueue
        # Define value ordering for the queue; this modifies ListNode globally.
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        dummy = curr = ListNode()
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put(node)
        while not q.empty():
            node = q.get()
            curr.next = node
            curr = curr.next
            if node.next:
                q.put(node.next)
        return dummy.next
    
    def mergeKLists_dc(self, lists: List[ListNode]) -> ListNode:
        """
        Merge adjacent groups in rounds, doubling the group size each round.
        Store each merged head at its leftmost input index and reuse nodes.
        k = number of linked lists, N = total number of nodes.
        Time Complexity: O(k + N * log(k + 1)), including empty-list merges
        Space Complexity: O(1) auxiliary space; iterative, with no recursion
        """
        k = len(lists)
        interval = 1  # distance between the starting indices of paired groups
        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if k > 0 else None
    
    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Relink the smaller head repeatedly, then attach the remaining suffix.
        m and n are the two input lengths.
        Time Complexity: O(m + n)
        Space Complexity: O(1) auxiliary space
        """
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next


def main():
    while True:
        try:
            line = input()
            nodes = stringToList(line)
            lists = [stringToListNode(l) for l in nodes]
            lists2 = [stringToListNode(l) for l in nodes]
            lists3 = [stringToListNode(l) for l in nodes]
            lists4 = [stringToListNode(l) for l in nodes]
            
            sol = Solution()
            ret_c = sol.mergeKLists_compare(lists)
            ret_hq = sol.mergeKLists_heapq(lists2)
            ret_pq = sol.mergeKLists_pq(lists3)
            ret_dc = sol.mergeKLists_dc(lists4)
            
            out_c = listNodeToString(ret_c)
            out_hq = listNodeToString(ret_hq)
            out_pq = listNodeToString(ret_pq)
            out_dc = listNodeToString(ret_dc)
            print(f"Solved by comparing all head nodes: {out_c}")
            print(f"Solved using heapq:                 {out_hq}")
            print(f"Solved using PriorityQueue:         {out_pq}")
            print(f"Solved using divide and conquer:    {out_dc}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
