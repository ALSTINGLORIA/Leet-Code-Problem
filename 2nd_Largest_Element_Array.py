class Solution:
    def secondLargestElement(self, nums):
        if not nums:
            return None
        curr1 = nums[0]
        curr2 = float('-inf')
        for val in nums:
            if curr1 < val:
                curr2 = curr1
                curr1 = val
            elif curr1 > val and curr2 < val:
                curr2 = val

        if curr2 == float('-inf'):
            return -1
        return curr2

            
