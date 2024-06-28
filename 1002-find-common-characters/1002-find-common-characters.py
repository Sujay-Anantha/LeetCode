class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
         # Initialize the counter with the first word
        common_count = Counter(words[0])
        
        # Intersect the counter with the rest of the words
        for word in words[1:]:
            word_count = Counter(word)
            common_count &= word_count  # Keep only the minimum counts
        
        # Convert the counter to the resulting list
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result