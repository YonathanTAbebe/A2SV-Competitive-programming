class Solution(object):
    def twoSum(self, nums, target):
        pre = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in pre:
                return [pre[diff], i]
            pre[n] = i
