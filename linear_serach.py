class Solution:
    def linearSearch(self, nums, target):
        for val in range(len(nums)):
            if nums[val] == target:
                return val
        return -1
