class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is empty, return 0
        if not needle:
            return 0
        
        # Generate the longest prefix suffix (LPS) array for the needle
        def computeLPSArray(needle):
            m = len(needle)
            lps = [0] * m
            length = 0  # Length of the previous longest prefix suffix
            i = 1

            while i < m:
                if needle[i] == needle[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        # KMP algorithm to search for needle in haystack
        n = len(haystack)
        m = len(needle)
        lps = computeLPSArray(needle)
        
        i = 0  # Index for haystack
        j = 0  # Index for needle
        
        while i < n:
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            
            if j == m:
                return i - j
            elif i < n and needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1

        