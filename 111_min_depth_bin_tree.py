from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root: return depth
        level = [root]
        while len(level) > 0:
            depth += 1
            next_level = []
            for node in level:
                if self.is_leaf(node): return depth
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            level = next_level
        return depth
    def is_leaf(self, node: TreeNode) -> bool:
        return not node.left and not node.right