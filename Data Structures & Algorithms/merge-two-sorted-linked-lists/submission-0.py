# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if the first list is empty, return second list
        if not list1: return list2
        if not list2: return list1 # and viceversa

        # otherwise, they both have values
        if list1.val <= list2.val: anchor, list1 = list1, list1.next
        else: anchor, list2 = list2, list2.next

        head = anchor

        while list1 and list2:
            if list1.val <= list2.val:
                anchor.next = list1
                list1 = list1.next
            else:
                anchor.next = list2
                list2 = list2.next
            anchor = anchor.next

        if not list1: anchor.next = list2
        else: anchor.next = list1

        return head


    