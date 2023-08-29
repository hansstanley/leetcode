from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        p1, p2 = headA, headB
        b1, b2 = True, True
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
            if p1 is None and b1:
                p1 = headB
                b1 = False
            if p2 is None and b2:
                p2 = headA
                b2 = False
        return None
