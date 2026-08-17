class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for val in range(1,len(nums)):
            if nums[val] != nums[val-1]:
                nums[left] = nums[val]
                left += 1
        k = left
        return  k

        
