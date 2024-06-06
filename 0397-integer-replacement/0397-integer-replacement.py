class Solution:
    def __init__(self):
        self.memo = {}

    def integerReplacement(self, n: int) -> int:
        return self.helper(n)

    def helper(self, n: int) -> int:
        if n == 1:
            return 0
        if n in self.memo:
            return self.memo[n]

        if n % 2 == 0:
            result = 1 + self.helper(n // 2)
        else:
            result = 1 + min(self.helper(n + 1), self.helper(n - 1))

        self.memo[n] = result
        return result