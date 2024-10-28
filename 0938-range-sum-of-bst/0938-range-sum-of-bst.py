class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        cum_sum = 0
        
        # Check if the current node value is within range
        if low <= root.val <= high:
            cum_sum += root.val

        # Traverse the left subtree if there's a chance of finding values within range
        if root.val > low:
            cum_sum += self.rangeSumBST(root.left, low, high)

        # Traverse the right subtree if there's a chance of finding values within range
        if root.val < high:
            cum_sum += self.rangeSumBST(root.right, low, high)
        
        return cum_sum
