from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        prev = None
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            prev = curr
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)
        