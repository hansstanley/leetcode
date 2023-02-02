# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes: List[ListNode] = []
        curr = head
        while curr is not None:
            nodes.append(curr)
            curr = curr.next
        nodes[-n].next = None
        new_next = None if n == 1 else nodes[-n + 1]

        if n == len(nodes): return new_next
        nodes[-n - 1].next = new_next
        return head