from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root: return None
        if depth == 1:
            new_root = TreeNode(val, root)
            return new_root
        if depth == 2:
            root.left, root.right = TreeNode(val, left=root.left), TreeNode(val, right=root.right)
            return root
        self.addOneRow(root.left, val, depth - 1)
        self.addOneRow(root.right, val, depth - 1)
        return root