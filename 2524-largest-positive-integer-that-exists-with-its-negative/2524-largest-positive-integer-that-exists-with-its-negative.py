class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Use a set for fast lookup
        seen = set()
        max_k = -1  # Initialize with -1, to return when no valid result is found

        for num in nums:
            seen.add(num)  # Add current number to the set
        
        for num in nums:
            if num > 0 and -num in seen:
                max_k = max(max_k, num)
        
        return max_k
