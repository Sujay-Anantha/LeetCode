class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for word in strs:
            # Sort the word to get the "signature"
            sorted_word = ''.join(sorted(word))
            
            # Add the word to the corresponding anagram group
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
        
        # Return all the grouped anagrams
        return list(anagrams.values())