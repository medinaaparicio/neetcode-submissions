# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # brute force
        # push everything onto a stack
        # for each value, pop off from the stack and calc sum 
        elem = head
        stack = []
        while elem:
            stack.append(elem.val)
            elem = elem.next
        pair = head
        best = 0
        while pair and pair.next:
            best = max(best, pair.val + stack.pop())
            pair = pair.next
        return best



        
        
