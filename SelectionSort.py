class Solution:
    def selectionSort(self, nums):
        start = 0
        while start < len(nums)-1:
            min_val = nums[start]
            min_pos = start 
            for val in range(start+1,len(nums)):
                if nums[val] < min_val:
                    min_val = nums[val]
                    min_pos = val
            temp = nums[start]
            nums[start] = min_val
            nums[min_pos] = temp
            start = start + 1
        return nums
