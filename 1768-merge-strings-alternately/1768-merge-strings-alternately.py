class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1) , len(word2)
        merged = ""
        for i in range (min(m,n)):
            
            merged += word1[i]+word2[i]
            print (merged)
        
        if m > n:
            merged = merged + word1[n:]
        if n>m:
            merged = merged + word2[m:]
        
        return merged