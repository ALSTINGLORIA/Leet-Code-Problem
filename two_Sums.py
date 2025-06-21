class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finish  = False
        indice = []
        while True:
            for size in range(len(nums)):

                for element in range(len(nums)):
                    if size != element:
                        if nums[size] + nums[element] == target:
                            indice.append(size)
                            indice.append(element)
                            finish = True
                            break
                if finish == True:
                    break
            if finish == True:
                break

        return indice