class Solution:
    def sortColors(self, nums: list[int]) -> None:
        p1 = 0 
        p2 = len(nums)-1
        val = 0
        while val <= p2:
            if nums[val] == 1:
                val += 1
            elif nums[val] == 0:
                nums[val],nums[p1] = nums[p1],nums[val]
                p1 += 1
                val += 1
            elif nums[val] == 2:
                nums[val],nums[p2] = nums[p2],nums[val]
                p2 -= 1
        return nums


        
