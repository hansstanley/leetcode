from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = dict[int, set[int]]()
        for i in range(n):
            tree[i] = set()
        for e in edges:
            tree[e[0]].add(e[1])
            tree[e[1]].add(e[0])
        while len(tree) > 2:
            to_prune = list[int]()
            for node, neighbours in tree.items():
                if len(neighbours) == 1:
                    to_prune.append(node)
            for node in to_prune:
                for neighbour in tree[node]:
                    tree[neighbour].remove(node)
                tree.pop(node)
        return list(tree.keys())


print(
    Solution().findMinHeightTrees(
        6,
        [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]],
    )
)
