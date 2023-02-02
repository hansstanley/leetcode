from typing import Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, set([p.val, q.val]))
    def dfs(self, root: 'TreeNode', nodes: Set[TreeNode]):
        if not root: return None
        l_ancestor = self.dfs(root.left, nodes)
        l_rem = len(nodes)
        r_ancestor = self.dfs(root.right, nodes)
        r_rem = len(nodes)
        nodes.discard(root.val)
        if l_rem == 0:
            return l_ancestor
        elif len(nodes) == 0:
            return r_ancestor if r_rem == 0 else root
        else:
            return None