class Solution:
    def isSorted(self, nums):
        if not nums:
            return None
        curr = nums[0]
        for val in nums:
            if curr > val:
                return False
            curr = val
        return True
