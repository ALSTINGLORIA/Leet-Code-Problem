class Solution:
    def insertionSort(self, nums):
        end = 0
        while end < len(nums):
            for p1 in range(end,0,-1):
                if nums[p1-1] > nums[p1]:
                    nums[p1-1],nums[p1] = nums[p1],nums[p1-1]
                elif nums[p1-1] < nums[p1]:
                    break
            end = end + 1    
        return nums
