class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        count = 0
        
        for i in range(n):
            # Check if the current element is greater than the next (next element is circular)
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        
        # If there is exactly one place where nums[i] > nums[i+1], it's a sorted and rotated array
        return count == 1 or (count == 0 and nums[0] >= nums[-1])