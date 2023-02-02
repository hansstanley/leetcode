# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = (p, q) if p.val < q.val else (q, p)
        curr = root
        while not (p.val <= curr.val <= q.val):
            curr = curr.left if curr.val > q.val else curr.right
        return curr