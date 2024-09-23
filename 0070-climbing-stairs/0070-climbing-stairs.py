class Solution:
    def climbStairs(self, n: int) -> int:
# Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Variables to store the number of ways to reach the previous two steps
        prev2 = 1  # ways to reach step 1
        prev1 = 2  # ways to reach step 2
        
        # Calculate ways to reach from step 3 to step n
        for i in range(3, n + 1):
            current = prev1 + prev2  # ways(n) = ways(n-1) + ways(n-2)
            prev2 = prev1  # Move prev1 and prev2 up for the next iteration
            prev1 = current
        
        return prev1