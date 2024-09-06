class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter


        char_count = Counter(s)
        
       
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        
      
        return -1
