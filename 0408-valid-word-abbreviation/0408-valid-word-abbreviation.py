class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_idx = 0  # Pointer for word
        abbr_idx = 0  # Pointer for abbr
        
        while abbr_idx < len(abbr) and word_idx < len(word):
            if abbr[abbr_idx].isalpha():
                # If abbr has a letter, it must match the word's current letter
                if abbr[abbr_idx] != word[word_idx]:
                    return False
                word_idx += 1
                abbr_idx += 1
            else:
                # If abbr has a digit, we need to skip that number of characters in word
                if abbr[abbr_idx] == '0':
                    return False  # Leading zeros are not allowed
                
                num = 0
                while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
                    num = num * 10 + int(abbr[abbr_idx])
                    abbr_idx += 1
                
                word_idx += num  # Skip 'num' characters in word
        
        # Both pointers should reach the end
        return word_idx == len(word) and abbr_idx == len(abbr)
        