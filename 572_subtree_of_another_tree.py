# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.recurse(root, subRoot, subRoot)
    def recurse(self, r1: Optional[TreeNode], r2: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not r1: return not r2
        if not r2: return not r1
        return (r1.val == r2.val and self.recurse(r1.left, r2.left, None) and self.recurse(r1.right, r2.right, None)) or self.recurse(r1.left, subRoot, subRoot) or self.recurse(r2.right, subRoot, subRoot)