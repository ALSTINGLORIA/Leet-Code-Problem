class Solution:
    def check(self, nums: List[int]) -> bool:
        arr_size = len(nums)
        window_size = 1
        start = 1
        while window_size < arr_size and start < (2*arr_size):
            if nums[start % arr_size] >= nums[(start % arr_size)-1]:
                window_size += 1
                start += 1
            elif nums[start % arr_size] < nums[(start % arr_size)-1]:
                start += 1
                window_size = 1

        if window_size == arr_size:
            return True
        else:
            return False







