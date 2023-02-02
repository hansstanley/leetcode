from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right: return [str(root.val)]
        l_paths = [f'{str(root.val)}->{p}' for p in self.binaryTreePaths(root.left)] if root.left else []
        r_paths = [f'{str(root.val)}->{p}' for p in self.binaryTreePaths(root.right)] if root.right else []
        return l_paths + r_paths