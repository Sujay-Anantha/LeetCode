class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
         # Convert string to a list of characters for easy modification
        s = list(s)
        n = len(s)
        
        # Apply shifts cumulatively from the end to the beginning
        total_shifts = 0
        for i in range(n - 1, -1, -1):
            total_shifts += shifts[i]
            total_shifts %= 26  # To handle large values and wrap around the alphabet
            
            # Shift the current character
            s[i] = chr((ord(s[i]) - ord('a') + total_shifts) % 26 + ord('a'))
        
        # Convert the list of characters back to a string
        return ''.join(s)