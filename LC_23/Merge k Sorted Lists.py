"""
Given an array of linked-lists lists, each linked list is sorted in ascending
order.

Merge all the linked-lists into one sort linked-list and return it.
"""
from typing import List, Tuple
from common_funcs import ListNode, stringToList, stringToListNode, listNodeToString


class Solution:
    def mergeKLists_compare(self, lists: List[ListNode]) -> ListNode:
        """
        Compare every k nodes (head of every linked list) and get the node with
        the smallest value. Extend the final sorted linked list with the
        selected nodes.
        Time Complexity: O(kN), k = # of linked-lists, N = total # of nodes
        Space Complexity: O(1)
        """
        
        def compare_nodes(nodes: List[ListNode]) -> Tuple[ListNode, int]:
            min_node, min_index = ListNode(val=float('inf')), 0
            for i, node in enumerate(nodes):
                if node and node.val < min_node.val:
                    min_node, min_index = node, i
            return min_node, min_index
        
        dummy = curr = ListNode()
        while any(node for node in lists):
            minN, minI = compare_nodes(lists)  # find min node and its index
            curr.next = minN  # append min node to curr
            lists[minI] = lists[minI].next  # move min node to next node
            curr = curr.next  # move curr pointer to next
        return dummy.next

    def mergeKLists_heapq(self, lists: List[ListNode]) -> ListNode:
        """
        k = # of linked-lists, N = total # of nodes
        Time Complexity: O(log(k)*N)
        Space Complexity: O(k)
        """
        import heapq
        # push all head nodes onto a heap
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        
        dummy = curr = ListNode()
        while heap:
            # heappop returns the node w/ the min val
            # i serves as a tie-breaker in case two nodes w/ the same val
            val, i, node = heapq.heappop(heap)
            curr.next = node  # append min node to curr
            curr = curr.next  # move curr pointer to next
            if node.next:  # push next if node has next node (not last one)
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
    
    def mergeKLists_pq(self, lists: List[ListNode]) -> ListNode:
        """
        k = # of linked-lists, N = total # of nodes
        Time Complexity: O(log(k)*N)
        Space Complexity: O(k)
        """
        from queue import PriorityQueue
        # provide __lt__ method to ListNode for PriorityQueue to work
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
        k = # of linked-lists, N = total # of nodes
        Time Complexity: O(log(k)*N)
        Space Complexity: O(1)
        """
        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if k > 0 else None
    
    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
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
