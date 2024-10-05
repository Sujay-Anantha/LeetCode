class Solution:
    def isPalindrome(self, s: str) -> bool:
        #U- Understand
        #M- Match
        #P- Plan
        #i- implement
        #r- review
        #e- execute
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '',s)
        
        l,r = 0,len(s)-1
        print(s)
        while l<r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True
            
            