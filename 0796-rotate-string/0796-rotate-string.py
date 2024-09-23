class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # if s == goal:
        #     return True
        # for i in range(1,len(s)):
        #     rearrange = s[i:]+s[0:i]
        #     if rearrange == goal:
        #         return True
        # return False
        
        # Check if the lengths of s and goal are the same
        if len(s) != len(goal):
            return False
        # Check if goal is a substring of s concatenated with itself
        return goal in s + s