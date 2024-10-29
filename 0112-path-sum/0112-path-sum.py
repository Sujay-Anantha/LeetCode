# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        def has_path_sum(root, target_sum):
            if root is None:
                return False
            if not root.left and not root.right:
                return target_sum == root.val
            return (has_path_sum(root.left, target_sum - root.val) or
                        has_path_sum(root.right, target_sum - root.val))
        return has_path_sum(root,target_sum)

        