class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]  # Reverse the list to make addition easier
        
        for i in range(len(digits)):
            if digits[i] != 9:
                digits[i] += 1
                return digits[::-1]  # Reverse back and return
            else:
                digits[i] = 0
        
        # If we are here, it means all digits were 9 and have turned into 0
        digits.append(1)  # Append the carry-over 1
        return digits[::-1]  # Reverse back and return
