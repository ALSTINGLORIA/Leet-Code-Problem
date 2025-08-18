class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(0,len(numbers)-1):
            check = target - numbers[i]
            if check in numbers[i+1:]:
                count = i
                for x in numbers[i+1:]:
                    count += 1
                    if check == x:
                        return [i+1,count+1]
