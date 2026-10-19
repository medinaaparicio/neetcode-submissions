# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # in case list is empty
        if not head:
            return head

        prev, curr = None, head

        while curr:
            following = curr.next
            curr.next = prev
            prev = curr
            curr = following


        return prev
        
        