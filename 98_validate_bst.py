from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], l: int = None, r: int = None) -> bool:
        if not root: return True
        if l is not None and root.val <= l: return False
        if r is not None and root.val >= r: return False
        return self.isValidBST(root.left, l, root.val) and self.isValidBST(root.right, root.val, r)

Solution().isValidBST(None)