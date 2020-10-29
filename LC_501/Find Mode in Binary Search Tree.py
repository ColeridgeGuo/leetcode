"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most
frequently occurred element) in the given BST.
"""
from typing import List
from collections import defaultdict
from common_funcs import TreeNode, stringToTreeNode, listToString


class Solution:
    def helper(self, root: TreeNode, count: defaultdict) -> None:
        if root:
            self.helper(root.left, count)
            self.helper(root.right, count)
            count[root.val] += 1
            
    def findMode(self, root: TreeNode) -> List[int]:
        """
            Use a counter to keep track of frequencies of all numbers in BST.
        """
        if not root:
            return []
        cnt = defaultdict(int)
        self.helper(root, cnt)
        max_freq = cnt[max(cnt, key=cnt.get)]
        modes = [n for n in cnt if cnt[n] == max_freq]
        return modes


class Solution2:
    # instance variables for method 2
    prev = None
    max_count = 0
    count = 0
    result = []
    
    def findMode(self, root: TreeNode) -> List[int]:
        """
        Inorder traversal of a BST will find the nodes in ascending order. So
        just compare the current node to the previous, and if they match,
        increase the current count of duplicate values by 1. If they don't
        match, reset the current count to 1. Compare the current count to the
        max count found so far. If they match, append the current value to the
        result list. If the current count of duplicates exceeds the max count,
        create a new result list with just the current value.
        """
        self.dfs(root)
        return self.result
    
    def dfs(self, node: TreeNode):
        if node:
            self.dfs(node.left)
            self.count = 1 if node.val != self.prev else self.count + 1
            if self.count == self.max_count:
                self.result.append(node.val)
            elif self.count > self.max_count:
                self.result = [node.val]
                self.max_count = self.count
            self.prev = node.val
            self.dfs(node.right)


class Solution3:
    prev = None
    curr_count = 0
    max_count = 0
    mode_count = 0
    modes = None
    
    def findMode(self, root: TreeNode) -> List[int]:
        """
        Two passes: one to find the highest number of occurrences of any value,
        and then a second pass to collect all values occurring that often.
        """
        self.inorder(root)
        self.modes = [0] * self.mode_count
        self.mode_count = 0
        self.curr_count = 0
        self.inorder(root)
        return self.modes
    
    def inorder(self, root: TreeNode):
        if root:
            self.inorder(root.left)
            self.handleValue(root.val)
            self.inorder(root.right)
            
    def handleValue(self, val: int):
        if val != self.prev:
            self.prev = val
            self.curr_count = 0
        self.curr_count += 1
        if self.curr_count > self.max_count:
            self.max_count = self.curr_count
            self.mode_count = 1
        elif self.curr_count == self.max_count:
            if self.modes:
                self.modes[self.mode_count] = self.prev
            self.mode_count += 1


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            root2 = stringToTreeNode(line)
            root3 = stringToTreeNode(line)

            ret = Solution().findMode(root)
            ret2 = Solution2().findMode(root2)
            ret3 = Solution3().findMode(root3)
            
            out = listToString(ret)
            out2 = listToString(ret2)
            out3 = listToString(ret3)
            print(out)
            print(out2)
            print(out3)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
