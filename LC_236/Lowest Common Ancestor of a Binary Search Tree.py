"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in
the tree.
Note:
    All of the nodes' values will be unique.
    p and q are different and both values will exist in the binary tree.
"""
from common_funcs import TreeNode


class Solution:
    def lowestCommonAncestor_recursive(self,
                                       root: 'TreeNode',
                                       p: 'TreeNode',
                                       q: 'TreeNode') -> 'TreeNode':
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        if root in (None, p, q):
            return root
        lca_left = self.lowestCommonAncestor_recursive(root.left, p, q)
        lca_right = self.lowestCommonAncestor_recursive(root.right, p, q)
        if lca_left and lca_right:
            return root
        if not lca_left and not lca_right:
            return lca_left
        if not lca_left:
            return lca_right
        else:
            return lca_left
    
    def lowestCommonAncestor_iterative(self,
                                       root: 'TreeNode',
                                       p: 'TreeNode',
                                       q: 'TreeNode') -> 'TreeNode':
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parents = {root: None}
        
        # Iterate until we find both the nodes p and q
        while not (p in parents and q in parents):
            curr = stack.pop()
            
            # While traversing the tree, keep saving the parent pointers.
            if curr.left:
                stack.append(curr.left)
                parents[curr.left] = curr
            if curr.right:
                stack.append(curr.right)
                parents[curr.right] = curr
                
        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parents[p]
            
        # The first ancestor of q that appears in p's ancestors is their LCA
        while q not in ancestors:
            q = parents[q]
        return q


def stringToTreeNode(input, p_val, q_val):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None
    
    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    p = root if p_val == int(inputValues[0]) else None
    q = root if q_val == int(inputValues[0]) else None
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
            p = node.left if p_val == leftNumber else p
            q = node.left if q_val == leftNumber else q
            nodeQueue.append(node.left)
        
        if index >= len(inputValues):
            break
        
        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            p = node.right if p_val == rightNumber else p
            q = node.right if q_val == rightNumber else q
            nodeQueue.append(node.right)
    return root, p, q


def main():
    while True:
        try:
            line = input()
            p_val = int(input())
            q_val = int(input())
            root, p, q = stringToTreeNode(line, p_val, q_val)
            
            sol = Solution()
            ret_recur = sol.lowestCommonAncestor_recursive(root, p, q)
            ret_iter = sol.lowestCommonAncestor_iterative(root, p, q)
            
            print(f"LCA found recursively: {ret_recur}")
            print(f"LCA found iteratively: {ret_iter}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
