# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # define a list that will contain postorder values
        container: list = []

        # recursive funtion
        def travers(root):
            nonlocal container
            # post order meanse root will run last time
            if root:
                travers(root.left)
                travers(root.right)
                container.append(root.value)

        travers(root)
        return container
