class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        merged = []
        
        # Merge the characters alternately
        for i in range(min(m, n)):
            merged.append(word1[i])
            merged.append(word2[i])
        
        # Add the remaining part of the longer string
        if m > n:
            merged.append(word1[n:])
        elif n > m:
            merged.append(word2[m:])
        
        # Join the list into a single string
        return ''.join(merged)