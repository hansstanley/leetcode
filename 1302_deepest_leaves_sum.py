# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        result = 0
        frontier = [root]
        while len(frontier) > 0:
            next_frontier = []
            for node in frontier:
                if node and node.left:
                    next_frontier.append(node.left)
                if node and node.right:
                    next_frontier.append(node.right)
            if len(next_frontier) == 0:
                result = sum([node.val for node in frontier if node])
            frontier = next_frontier
        return result
