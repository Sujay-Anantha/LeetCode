class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # When a mismatch occurs, check the two possible cases:
                # 1. Skip the left character (l+1)
                # 2. Skip the right character (r-1)
                
                # Check if skipping s[l] or s[r] results in a palindrome
                skip_left = s[l+1:r+1]  # Substring after skipping left character
                skip_right = s[l:r]      # Substring after skipping right character
                
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
        
        return True
        