class Solution:
    def bubbleSort(self, nums):
        for p1 in range(len(nums)):
            swapped = False
            for p2 in range(1,len(nums)-p1):
                if nums[p2] < nums[p2-1]:
                    nums[p2],nums[p2-1] = nums[p2-1],nums[p2]
                    swapped = True
            if swapped == False:
                break

        return nums
                     
