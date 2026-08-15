# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        # Store the preorder traversal here.
        result = []

        def dfs(node):
            # If there is no node, record "null".
            #
            # We MUST store null because otherwise we would
            # lose information about the tree's structure.
            if not node:
                result.append("null")
                return

            # Record the current node first.
            # This is preorder: ROOT -> LEFT -> RIGHT
            result.append(str(node.val))

            # Serialize the left subtree.
            dfs(node.left)

            # Serialize the right subtree.
            dfs(node.right)

        # Start DFS from the root.
        dfs(root)

        # Convert the list into one string.
        return ",".join(result)

    def deserialize(self, data):

        # Convert:
        #
        # "1,2,null,null,3,null,null"
        #
        # into:
        #
        # ["1", "2", "null", "null", "3", "null", "null"]
        values = data.split(",")

        # Points to the next value we need to process.
        index = 0

        def dfs():
            nonlocal index

            # If the current value is "null",
            # this child does not exist.
            if values[index] == "null":
                index += 1
                return None

            # Create a node using the current value.
            node = TreeNode(int(values[index]))

            # Move to the next serialized value.
            index += 1

            # The next values describe the left subtree.
            node.left = dfs()

            # After the left subtree is finished,
            # the next values describe the right subtree.
            node.right = dfs()

            # Return the completed subtree.
            return node

        # Reconstruct the tree starting from the first value.
        return dfs()
        



