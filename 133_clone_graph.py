"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        clones = {}
        def traverse(node: 'Node') -> 'Node':
            if node.val in clones: return clones[node.val]
            clones[node.val] = Node(node.val)
            clones[node.val].neighbors = [traverse(neighbor) for neighbor in node.neighbors]
            return clones[node.val]
        return traverse(node)

# class Solution:
#     def cloneGraph(self, node: 'Node', memo = {}) -> 'Node':
#         if not Node: return None
#         memo[node.val] = Node(node.val)
#         memo[node.val].neighbours = [memo.get(n.val) or self.cloneGraph(n, memo) for n in node.neighbors]
#         return memo[node.val]
#         new_node = Node(node.val)
#         if parent:
#             new_node.neighbors = [parent if n.val == parent.val else self.cloneGraph(n, new_node) for n in node.neighbors]
#         else:
#             new_node.neighbors = [self.cloneGraph(n, new_node) for n in node.neighbors]
#         return new_node