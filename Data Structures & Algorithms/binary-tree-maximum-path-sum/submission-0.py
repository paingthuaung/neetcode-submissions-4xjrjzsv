# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        self.res = float("-inf")

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Best complete path passing through this node
            self.res = max(
                self.res,
                left + node.val + right
            )

            # Best path that can be extended by the parent
            return node.val + max(left, right)

        dfs(root)
        return self.res