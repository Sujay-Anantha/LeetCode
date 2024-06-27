class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last_seen = {}
        left,max_length = 0, 0

        for right in range(0,len(s)):
            char = s[right]
            if char in last_seen and last_seen[char] >= left:
                #seen it and is it in the current window
                left = last_seen[char] + 1

            #update max len
            max_length = max(max_length,right-left+1)      
            last_seen[char] = right

        return max_length
                
            
                
            
        