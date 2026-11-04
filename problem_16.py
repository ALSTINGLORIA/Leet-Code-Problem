class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        small = float('inf')
        p1 = 0
        p2 = 1
        p3 = len(nums)-1
        final = 0
        while p1 < p3-1:
            while p2 < p3:
                sum1 = nums[p1] + nums[p2] + nums[p3]
                close = abs(sum1 - target)
                if small > close:
                    small = close
                    final = sum1
                if sum1 < target:
                    p2 += 1
                elif sum1 > target:
                    p3 -= 1
                else:
                    return sum1
            p1 += 1
            p2 = p1 + 1
            p3 = len(nums)-1
        return final
