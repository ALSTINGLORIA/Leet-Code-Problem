class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        p1 = 0
        p2 = len(numbers)-1

        while p1 < p2:
            sum = numbers[p1] + numbers[p2]
            if sum > target:
                p2 = p2 - 1
            elif sum < target:
                p1 = p1 + 1
            else:
                return [p1+1,p2+1]
        
