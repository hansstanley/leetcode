from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        met_zero = False
        while head is not None:
            if head.val == 0:
                if met_zero:
                    return True
                met_zero = True
            head.val = 0
            head = head.next
        return False
