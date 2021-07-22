from typing import List, Union
RecurList = List[Union[int, 'RecurList']]


# ###################  TreeNode  ################### #
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.val}'

    def __repr__(self) -> str:
        return f"{self.val}"


# convert input string to TreeNode
def stringToTreeNode(input: str) -> TreeNode:
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


# convert output TreeNode to string
def treeNodeToString(root: TreeNode) -> str:
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
# convert input string to list
def stringToList(input: str) -> RecurList:
    import json
    return json.loads(input)


# convert output list to string
def listToString(nums: RecurList, len_of_list: int = None) -> str:
    import json
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


# ###################  string <=> string  ################### #
# convert input string to string
def stringToString(input: str) -> str:
    import json
    return json.loads(input)


# convert output string to string
def stringToString_out(input: str) -> str:
    import json
    return json.dumps(input)


# ###################  ListNode  ################### #
# ListNode class
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}"

    def __repr__(self) -> str:
        return f"{self.val}"


# convert input string to ListNode
def stringToListNode(input: str) -> ListNode:
    # Generate list from the input
    if isinstance(input, str):
        numbers = stringToList(input)
    else:
        numbers = input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    return dummyRoot.next


# convert output ListNode to string
def listNodeToString(node: ListNode) -> str:
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"
