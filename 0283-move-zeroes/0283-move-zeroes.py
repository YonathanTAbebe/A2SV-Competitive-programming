class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0  # pointer for the next position of non-zero element
        for right in range(len(nums)):
            if nums[right] != 0:
                # Swap nums[left] with nums[right] if nums[right] is non-zero
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
