class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        postfix = 1
        output = []
        for x in range(len(nums)):
            output.append(prefix)
            prefix *= nums[x]

        for y in range(len(nums)-1,-1,-1):
            output[y] *= postfix
            postfix *= nums[y]

        return output

            
