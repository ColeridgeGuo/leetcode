"""
Given a non-empty special binary tree consisting of nodes with the non-negative
value, where each node in this tree has exactly two or zero sub-node. If the
node has two sub-nodes, then this node's value is the smaller value among its
two sub-nodes. More formally, the property
    root.val = min(root.left.val, root.right.val)
always holds.
Given such a binary tree, you need to output the second minimum value in the set
made of all the nodes' value in the whole tree. If no such second minimum value
exists, output -1 instead.
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans = float('inf')
        min1 = root.val

        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)
                    
        dfs(root)
        return self.ans if self.ans < float('inf') else -1


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            
            sol = Solution()
            ret = sol.findSecondMinimumValue(root)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
