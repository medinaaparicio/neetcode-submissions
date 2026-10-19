# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = -1
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if fast == slow:
                index = slow
                break
        return index != -1

        