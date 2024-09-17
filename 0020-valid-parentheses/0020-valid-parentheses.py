class Solution:
    def isValid(self, s: str) -> bool:
            # Stack to keep track of opening brackets
        stack = []

        # Dictionary to match closing brackets with their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        # Traverse through each character in the string
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'

                # Check if the popped element is the matching opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)

        # If the stack is empty, all opening brackets were properly closed
        return not stack
        