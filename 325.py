# Note: This soluton will fail on time exceeded (Brute Force)
class Solution:
    def longestSubarray(self, nums, k):
        largest = 0
        count = 0
        for val1 in range(len(nums)):
            count = 0
            sum1 = 0
            for val2 in range(val1,len(nums)):
                sum1 += nums[val2]
                count += 1
                if sum1 == k:
                    if largest < count:
                        largest = count 

        return largest
