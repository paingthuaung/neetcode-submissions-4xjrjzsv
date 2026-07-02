# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            # save the next node before we change current.next
            temp = current.next
            # Reverse the current node's pointer
            current.next = prev
            # Move prev and current one step forward
            prev = current
            current = temp
        
        return prev