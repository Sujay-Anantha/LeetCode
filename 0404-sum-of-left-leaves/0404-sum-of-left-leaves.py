# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def Leftleaves(root):
            if root is None:
                return 0
            sum_left = 0
            # Check if the left child is a leaf
            if root.left and root.left.left is None and root.left.right is None:
                sum_left += root.left.val
            # Recurse on left and right children
            sum_left += Leftleaves(root.left)
            sum_left += Leftleaves(root.right)
            return sum_left
        
        return Leftleaves(root)
        