from common_funcs import ListNode


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    
    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list2.next, list1)
        return list2


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(2)
l5 = ListNode(5)
l6 = ListNode(6)

l1.next = l2
l2.next = l3
l4.next = l5
l5.next = l6

print(mergeTwoLists(l1, l4))
