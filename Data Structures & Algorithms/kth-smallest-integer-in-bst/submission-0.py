# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        self.cnt = 0
        def dfs(root):
            #Base case or early termination check
            if not root or self.cnt >= k:
                return 
            # process left
            dfs(root.left)
            # process current node
            self.cnt += 1
            
            if k == self.cnt:
                self.res = root.val
                return
            
            #process right
            dfs(root.right)
            
        dfs(root)
        return self.res
        
