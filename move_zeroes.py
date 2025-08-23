class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        point1 = 0
        while point1 < (len(nums)):
            if nums[point1] != 0:
                point1 +=1
            elif nums[point1] == 0:
                for x in range(point1+1,len(nums)):
                    if nums[x] != 0:
                        temp = nums[point1]
                        nums[point1] = nums[x]
                        nums[x] = temp
                        break
                point1 += 1


        
