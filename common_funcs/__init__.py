import json
from typing import List, Tuple

RecurList = List['int | str | RecurList']


# ###################  TreeNode  ################### #
class TreeNode:
    """
    Binary Tree Node class
    """

    def __init__(self, val: int = 0,
                 left: 'TreeNode' = None,
                 right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.val}'

    def __repr__(self) -> str:
        return f"{self.val}"


def stringToTreeNode(input_: str) -> TreeNode | None:
    """
    Converts input string to TreeNode
    """
    input_ = input_.strip()
    input_ = input_[1:-1]
    if not input_:
        return

    input_values = [s.strip() for s in input_.split(',')]
    root = TreeNode(int(input_values[0]))
    node_queue: List[TreeNode] = [root]
    front = 0
    index = 1
    while index < len(input_values):
        node = node_queue[front]
        front = front + 1

        item = input_values[index]
        index = index + 1
        if item != "null":
            left_number = int(item)
            node.left = TreeNode(left_number)
            node_queue.append(node.left)

        if index >= len(input_values):
            break

        item = input_values[index]
        index = index + 1
        if item != "null":
            right_number = int(item)
            node.right = TreeNode(right_number)
            node_queue.append(node.right)
    return root


def stringToTreeNode_pq(input_: str, p_val: int, q_val: int) -> Tuple[TreeNode, TreeNode, TreeNode] | None:
    """
    Converts input string to TreeNode with two nodes p and q in the tree.
    """
    input_ = input_.strip()
    input_ = input_[1:-1]
    if not input_:
        return None

    input_values = [s.strip() for s in input_.split(',')]
    root = TreeNode(int(input_values[0]))
    p = root if p_val == int(input_values[0]) else None
    q = root if q_val == int(input_values[0]) else None
    node_queue = [root]
    front = 0
    index = 1
    while index < len(input_values):
        node = node_queue[front]
        front = front + 1

        item = input_values[index]
        index = index + 1
        if item != "null":
            left_number = int(item)
            node.left = TreeNode(left_number)
            p = node.left if p_val == left_number else p
            q = node.left if q_val == left_number else q
            node_queue.append(node.left)

        if index >= len(input_values):
            break

        item = input_values[index]
        index = index + 1
        if item != "null":
            right_number = int(item)
            node.right = TreeNode(right_number)
            p = node.right if p_val == right_number else p
            q = node.right if q_val == right_number else q
            node_queue.append(node.right)
    return root, p, q


def treeNodeToString(root: TreeNode) -> str:
    """
    Converts output TreeNode to string
    """
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    while output.endswith('null, '):
        output = output[:-6]
    return "[" + output[:-2] + "]"


# ###################  string <=> list  ################### #
def stringToList(input_: str) -> RecurList:
    """
    Converts input string to list (recursive)
    """
    return json.loads(input_)


def listToString(nums: RecurList, len_of_list: int = None) -> str:
    """
    Converts output list to string
    """
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


# ###################  string <=> string  ################### #
def stringToString(input_: str) -> str:
    """
    Converts input string to string
    """
    return json.loads(input_)


def stringToString_out(input_: str) -> str:
    """
    Converts output string to string
    """
    return json.dumps(input_)


# ###################  ListNode  ################### #
class ListNode:
    """
    List Node class
    """

    def __init__(self, val: int = 0, next_node: 'ListNode' = None) -> None:
        self.val = val
        self.next = next_node

    def __str__(self) -> str:
        return f"{self.val}"

    def __repr__(self) -> str:
        return f"{self.val}"


def stringToListNode(input_: str) -> ListNode:
    """
    Converts input string to ListNode
    """
    # Generate list from the input
    if isinstance(input_, str):
        numbers = stringToList(input_)
    else:
        numbers = input_

    # Now convert that list into linked list
    dummy_root = ListNode(0)
    ptr = dummy_root
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    return dummy_root.next


def listNodeToString(node: ListNode) -> str:
    """
    Converts output ListNode to string
    """
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"
