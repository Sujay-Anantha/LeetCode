class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        l, w = 0, 0
        
        while l < m and w < n:
            if s[l] == t[w]:
                l += 1  # Move to the next character in s only when there is a match
            w += 1  # Always move to the next character in t
            
        # If we have gone through all characters in s, it is a subsequence
        return l == m
            
            
        