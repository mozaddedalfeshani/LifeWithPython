# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # define a list that will store values as preorder
        ans: list = []

        def travers(root):
            nonlocal ans
            # preorder means root will first
            if root:
                ans.append(root.val)
                travers(root.left)
                travers(root.right)

        travers(root)
        return ans
