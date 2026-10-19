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
        # elem = head
        # stack = []
        # while elem:
        #     stack.append(elem.val)
        #     elem = elem.next
        # pair = head
        # best = 0
        # while pair and pair.next:
        #     best = max(best, pair.val + stack.pop())
        #     pair = pair.next
        # return best

        # their solution
        # 1. find the mid point
        # 2. mientras te mueves, algun half
        # 3. traverse it calculando

                # 1. find the middle of the linkedlist
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now slow marks the middle and last marks the end 
        middle, chopped = slow, slow.next
        prev = None
        # 2. reverse second half
        while chopped:
            nxt = chopped.next
            chopped.next = prev
            prev = chopped
            chopped = nxt
        # now prev holds the end of the reversed second half

        # 3. calculate the twin sums
        start = head
        best = 0
        while prev:
            best = max(best, start.val + prev.val)
            start, prev = start.next, prev.next
        return best



        
        
