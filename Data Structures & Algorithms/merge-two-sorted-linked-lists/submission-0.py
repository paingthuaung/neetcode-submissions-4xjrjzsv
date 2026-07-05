# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        # Create a dummy node to act as the start of the merged list
        dummy = ListNode(0)
        tail  = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                tail.next = l1 # Attach l1 to the merged list
                l1 = l1.next # Move l1 pointer forward
            else:
                tail.next = l2 # Attach l2 to the merged list
                l2 = l2.next # Move l2 pointer forward
            
            tail = tail.next # Move the merged list's tail forward
        # Append the remaining nodes of the non-empty list
        tail.next = l1 if l1 is not None else l2
        # Return the actual head of the merged list (skipping dummy)
        return dummy.next
                