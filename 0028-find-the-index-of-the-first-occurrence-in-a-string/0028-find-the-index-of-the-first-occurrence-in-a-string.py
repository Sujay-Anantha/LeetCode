class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        print(len(haystack))
        for i in range(len(haystack)):
            print(haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)] == needle:
                return i
            
        return -1
        