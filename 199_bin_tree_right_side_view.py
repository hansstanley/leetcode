from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode], level = 0, res = []) -> List[int]:
        if not root: return res
        if len(res) <= level:
            res.append(root.val)
        else:
            res[level] = root.val
        self.rightSideView(root.left, level + 1, res)
        self.rightSideView(root.right, level + 1, res)
        return res