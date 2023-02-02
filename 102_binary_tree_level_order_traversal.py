from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return res

        curr_level = [root]
        while len(curr_level) > 0:
            res.append([node.val for node in curr_level])
            next_level = []
            for node in curr_level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            curr_level = next_level
        return res