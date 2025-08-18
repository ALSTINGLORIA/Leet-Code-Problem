class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pivot = 0
        swap = len(nums)-1
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                pivot = i
                break
        if pivot == 0:
            nums = nums.sort()
        else:
            while nums[pivot-1] >= nums[swap]:
                swap -= 1
            temp = nums[swap]
            nums[swap] = nums[pivot - 1]
            nums[pivot-1] = temp

            nums[pivot:] = reversed(nums[pivot:])
            
