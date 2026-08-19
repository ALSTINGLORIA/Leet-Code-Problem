class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        step = 0
        curr = 0
        while curr < len(nums):
            if nums[curr] != 0:
                new_curr = curr
                count = 0
                while count < step:
                    nums[new_curr],nums[new_curr-1] = nums[new_curr-1],nums[new_curr]
                    new_curr -= 1
                    count += 1
            elif nums[curr] == 0:
                step += 1
            curr += 1

