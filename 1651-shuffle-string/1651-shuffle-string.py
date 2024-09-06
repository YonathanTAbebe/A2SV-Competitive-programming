from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Initialize a list with the same length as `s` to store characters in their correct positions
        restored = [''] * len(s)
        
        # Place each character from `s` into its new position based on `indices`
        for char, index in zip(s, indices):
            restored[index] = char
        
        # Join the list into a string and return it
        return ''.join(restored)
