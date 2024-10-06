class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        # Initialize the first two Fibonacci numbers
        a, b = 0, 1
        
        # Compute Fibonacci numbers iteratively
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b