class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))

        # Padding the shorter string with leading zeros
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        carry = 0
        result = []

        # Adding from the least significant digit to the most significant digit
        for i in range(max_len - 1, -1, -1):
            digit_a = int(a[i])
            digit_b = int(b[i])

            # Sum of digits and carry
            total = digit_a + digit_b + carry

            # Current digit is total modulo 2
            result.append(str(total % 2))

            # New carry is total divided by 2
            carry = total // 2

        # If there's a carry left at the end, append it
        if carry:
            result.append(str(carry))

        # Reverse the result since we've constructed it backwards
        result.reverse()

        return ''.join(result)            

        