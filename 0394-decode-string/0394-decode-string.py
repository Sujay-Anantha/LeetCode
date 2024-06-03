class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        char_stack = []
        current_num = 0
        current_string = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                num_stack.append(current_num)
                char_stack.append(current_string)
                current_num = 0
                current_string = ""
            elif char == ']':
                repeat_count = num_stack.pop()
                prev_string = char_stack.pop()
                current_string = prev_string + current_string * repeat_count
            else:
                current_string += char

        return current_string