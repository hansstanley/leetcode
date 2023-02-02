from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], is_left = False) -> int:
        if not root.left and not root.right: return root.val if is_left else 0
        sum = 0
        if root.left: sum += self.sumOfLeftLeaves(root.left, True)
        if root.right: sum += self.sumOfLeftLeaves(root.right, False)
        return sum