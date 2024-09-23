class Solution:
    def isPalindrome(self, x: int) -> bool:
# If the number is negative or if it ends with a zero (but is not zero), it's not a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            # Add the last digit of x to the reversed half
            reversed_half = reversed_half * 10 + x % 10
            # Remove the last digit from x
            x //= 10
        
        # The number is a palindrome if:
        # - The first half (x) is equal to the second half (reversed_half)
        # - or if the first half (x) is equal to reversed_half // 10 (for odd-length numbers)
        return x == reversed_half or x == reversed_half // 10
    