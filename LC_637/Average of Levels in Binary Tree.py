"""
Given a non-empty binary tree, return the average value of the nodes on each
level in the form of an array.
"""
from typing import List
from common_funcs import TreeNode, stringToTreeNode, listToString


class Solution:
    def averageOfLevels_bfs(self, root: TreeNode) -> List[float]:
        from collections import deque
        queue, res = deque([(root, 0)]), []
        level_sum, level_count = 0, 0
        while queue:
            node, curr_level = queue.popleft()
            if node.left:
                queue.append((node.left, curr_level + 1))
            if node.right:
                queue.append((node.right, curr_level + 1))
            level_sum, level_count = level_sum + node.val, level_count + 1
            if not queue or curr_level != queue[0][1]:
                # if current level is different from next node on queue or empty
                res.append(level_sum/level_count)
                level_sum, level_count = 0, 0
        return res

    def averageOfLevels_bfs_2(self, root: TreeNode) -> List[float]:
        from collections import deque
        queue, res = deque([root]), []
        level_sum = 0
        while queue:
            count = len(queue)
            for _ in range(count):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_sum/count)
            level_sum = 0
        return res
    
    def averageOfLevels_bfs_2b(self, root: TreeNode) -> List[float]:
        res, level = [], [root]
        while level:
            res.append(sum(node.val for node in level) / len(level))
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res

    def averageOfLevels_recursive(self, root: TreeNode) -> List[float]:
        res, count = [], []
        
        def average(t: TreeNode, i: int):
            if t:
                if i < len(res):
                    res[i] += t.val
                    count[i] += 1
                else:
                    res.append(t.val)
                    count.append(1)
                average(t.left, i + 1)
                average(t.right, i + 1)
                
        average(root, 0)
        for i in range(len(res)):
            res[i] = res[i] / count[i]
        return res


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            
            sol = Solution()
            ret = sol.averageOfLevels_bfs(root)
            ret_2 = sol.averageOfLevels_bfs_2(root)
            ret_2b = sol.averageOfLevels_bfs_2b(root)
            ret_r = sol.averageOfLevels_recursive(root)
            
            out = listToString(ret)
            out_2 = listToString(ret_2)
            out_2b = listToString(ret_2b)
            out_r = listToString(ret_r)
            print(f"Solved iteratively by checking level with next in queue: "
                  f"{out}")
            print(f"Solved iteratively using for loop for each level:        "
                  f"{out_2}")
            print(f"Solved iteratively with a more Pythonic style:           "
                  f"{out_2b}")
            print(f"Solved recursively:                                      "
                  f"{out_r}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
