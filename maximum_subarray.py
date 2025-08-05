class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        sum = 0
        
        for i in nums:
            if sum < 0:
                sum = 0
            sum += i
            if largest < sum:
                largest = sum

        return largest
