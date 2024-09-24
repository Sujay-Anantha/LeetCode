class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
         # Convert wordDict to a set for O(1) lookups
        word_set = set(wordDict)
        
        # DP array to store if s[0:i] can be segmented into words from wordDict
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string can always be segmented
        
        # Check every substring of s
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If s[0:j] can be segmented and s[j:i] is in the dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further if we found a valid segmentation
        
        return dp[len(s)]