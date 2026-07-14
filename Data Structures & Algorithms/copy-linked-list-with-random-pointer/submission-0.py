"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # If the input list is empty (None), there is nothing to copy, so return None
        if not head:
            return None
        
        # Initialize an empty dictionary to map original node objects to their new cloned twins
        hashmap = {}
        
        # --- STEP 1: CREATE COPIES OF ALL NODES ---
        
        # Create a temporary pointer 'current' starting at the head to traverse the original list
        current = head
        
        # Loop through the original list node-by-node until we reach the end (None)
        while current:
            # Instantiate a brand-new Node with the same value, but empty pointers (next=None, random=None).
            # Then, save it in the hashmap using the original node object as the lookup key.
            hashmap[current] = Node(current.val)
            
            # Move the 'current' pointer forward to the next node in the original list
            current = current.next
            
        # --- STEP 2: CONNECT NEXT AND RANDOM POINTERS ---
        
        # Reset the 'current' pointer back to the head of the original list for a second pass
        current = head
        
        # Loop through the original list a second time to use its layout as a wiring guide
        while current:
            # Fetch the corresponding cloned twin node from our hashmap
            copy = hashmap[current]
            
            # Use .get() to look up the clone of the original 'next' node.
            # If current.next is None (end of list), .get(None) safely returns None without crashing.
            copy.next = hashmap.get(current.next)
            
            # Use .get() to look up the clone of the original 'random' node.
            # Even if current.random points far ahead, its clone already exists in the map from Step 1.
            copy.random = hashmap.get(current.random)
            
            # Move the 'current' pointer forward to wire up the next cloned node in the loop
            current = current.next
        
        # Return the clone of the original head node, which serves as the entrance to the deep-copied list
        return hashmap[head]
