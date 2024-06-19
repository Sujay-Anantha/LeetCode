class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by spaces and filter out empty strings
        words = [word for word in s.split(' ') if word]
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join the reversed words with a single space
        return ' '.join(reversed_words)