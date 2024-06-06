class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        first = max(strs)
        end = min(strs)
        
        length = min(len(first),len(end))
        
        for i in range(0,length):
            if first[i] != end[i]:
                return first[0:i]
        return first[0:length]