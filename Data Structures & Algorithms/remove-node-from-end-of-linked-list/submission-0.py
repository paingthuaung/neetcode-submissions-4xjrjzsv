class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node pointing to the head.
        # This handles edge cases seamlessly, like when the list has only 1 node 
        # or when you need to delete the very first node (the head).
        dummy = ListNode(0, head)
        
        # 2. Initialize both fast and slow pointers at the dummy node.
        fast  = dummy
        slow  = dummy

        # 3. Advance the fast pointer forward by n + 1 steps.
        # This creates a strict physical gap of exactly n nodes between fast and slow.
        for _ in range(n + 1):
            fast = fast.next
        
        # 4. Move both pointers forward simultaneously at the same speed.
        # Because we maintain the gap, when the fast pointer reaches the end (None),
        # the slow pointer stops exactly BEFORE the node that needs to be deleted.
        while fast:
            fast = fast.next
            slow = slow.next

        # 5. Delete the target node by changing the pointer reference.
        # We skip slow.next (the target) and link directly to slow.next.next.
        slow.next = slow.next.next

        # 6. Return the actual head of the modified list.
        # dummy.next always points to the correct head, even if the original head was deleted.
        return dummy.next