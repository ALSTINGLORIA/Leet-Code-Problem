class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        p1 = 0
        p2 = 0
        sum1 = nums[0]
        small = float('inf')
        while p1 < len(nums):
            if sum1 >= target:
                if (p2 - p1+1) < small:
                    small = p2 - p1+1
                sum1 -= nums[p1]
                p1 += 1
            elif sum1 < target and p2 < len(nums)-1:
                p2 += 1
                sum1 += nums[p2]
            else:
                break
        if small == float('inf'):
            return 0
        return small

            
