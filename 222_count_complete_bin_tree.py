from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l, r = root.left, root.right
        l_count = r_count = 0
        while l:
            l_count += 1
            l = l.left
        while r:
            r_count += 1
            r = r.right
        if l_count == r_count:
            return 2**l_count - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)