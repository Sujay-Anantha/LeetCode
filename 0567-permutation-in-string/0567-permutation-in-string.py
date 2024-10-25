from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, s2 cannot contain a permutation of s1
        if len(s1) > len(s2):
            return False
        
        # Frequency count of characters in s1
        s1_count = Counter(s1)
        # Frequency count of the initial window in s2
        window_count = Counter(s2[:len(s1)])
        
        # Check if the initial window matches
        if s1_count == window_count:
            return True
        
        # Sliding window over the rest of s2
        for i in range(len(s1), len(s2)):
            # Add the new character to the window
            window_count[s2[i]] += 1
            # Remove the character that is sliding out of the window
            window_count[s2[i - len(s1)]] -= 1
            
            # Remove the character count if it reaches zero
            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]
            
            # Check if the current window matches s1_count
            if s1_count == window_count:
                return True
        
        return False
   