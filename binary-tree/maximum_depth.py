from typing import Optional
from collections import deque
from tree_node import TreeNode


class Solution:
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        """Iterative BFS -> 83ms 15.3MB"""
        if not root:
            return 0

        q = deque()
        q.append(root)
        depth = 0
        while q:
            level = len(q)
            depth += 1

            for _ in range(level):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return depth

    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        """Iterative DFS -> 99ms 15.3MB"""
        if not root:
            return 0

        stack = [[root, 1]]
        depth = 1
        while stack:
            node, curr_depth = stack.pop()

            if node:
                depth = max(depth, curr_depth)

            if node.left:
                stack.append([node.left, curr_depth + 1])
            if node.right:
                stack.append([node.right, curr_depth + 1])

        return depth

    def maxDepthRecursiveDFS(self, root: Optional[TreeNode]) -> int:
        """Recursive DFS -> 78ms 16.5MB"""
        if not root:
            return 0
        return 1 + max(self.maxDepthRecursiveDFS(root.left), self.maxDepthRecursiveDFS(root.right))
