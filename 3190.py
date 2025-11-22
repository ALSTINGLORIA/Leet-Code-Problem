class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for x in range(len(nums)):
            rem = nums[x]%3
            if rem == 1:
                nums[x] -= 1
                count += 1
            elif rem == 2:
                nums[x] += 1
                count += 1
        return count
