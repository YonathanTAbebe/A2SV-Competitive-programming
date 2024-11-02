class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        # Start from the last digit and move towards the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # Set current digit to 0 and carry over
        
        # If all digits were 9, we need an extra digit
        return [1] + digits