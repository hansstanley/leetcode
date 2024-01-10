from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next
            if fast.next:
                slow = slow.next
                fast = fast.next

        prev = slow
        if slow and prev:
            slow = slow.next
            prev.next = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev, slow = slow, temp

        tail = prev
        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True
