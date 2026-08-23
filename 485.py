class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        large = 0
        for val in nums:
            if val == 1:
                count += 1
            elif val == 0:
                if count > large:
                    large = count
                count = 0 
        if count > large:
            large = count
        return large

