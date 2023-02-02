from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        curr, count = head.next, 0
        while curr and curr.val == head.val:
            curr = curr.next
            count += 1
        if count > 0:
            return self.deleteDuplicates(curr)
        else:
            head.next = self.deleteDuplicates(curr)
            return head