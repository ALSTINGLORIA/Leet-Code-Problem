class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lock = 0
        curr = 0
        zero_p = 0
        while curr < len(nums):
       
            if nums[curr] == 0 and lock == 0:
                lock = 1

            elif nums[curr] != 0:
                nums[zero_p],nums[curr] = nums[curr],nums[zero_p]
                lock = 0
                zero_p += 1
            curr += 1




