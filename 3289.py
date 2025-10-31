class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        new_num = []
        for x in nums:
            if nums.count(x) == 2 and not(x in new_num):
                new_num.append(x)
        return new_num
