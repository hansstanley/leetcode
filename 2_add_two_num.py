from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry_over = False) -> Optional[ListNode]:
        if not l1 and not l2: return ListNode(1) if carry_over else None
        if l1 and l2:
            sum = l1.val + l2.val + carry_over
            return ListNode(sum % 10, self.addTwoNumbers(l1.next, l2.next, sum > 9))
        node = l1 or l2
        sum = node.val + carry_over
        return ListNode(sum % 10, self.addTwoNumbers(node.next, None, sum > 9))