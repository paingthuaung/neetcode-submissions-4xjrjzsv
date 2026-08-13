# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        hashmap = {value: index for index, value in enumerate(inorder)}
        self.pre_idx = 0
        def dfs(left, right):
            if left > right:
                return None
            node_val = preorder[self.pre_idx]
            root = TreeNode(node_val)
            self.pre_idx += 1

            mid = hashmap[node_val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root
        
        return dfs(0, len(inorder) - 1)


        

        