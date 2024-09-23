class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        for i in range(1,len(s)):
            rearrange = s[i:]+s[0:i]
            if rearrange == goal:
                return True
        return False