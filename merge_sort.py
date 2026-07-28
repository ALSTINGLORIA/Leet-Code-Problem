class Solution:
    def mergeSort(self, nums):
        def divide(arr,low,high):
            if low != high:
                mid = (low+high)//2
                divide(arr,low,mid)
                divide(arr,mid+1,high)
                merge(arr,low,mid,high)

        def merge(arr,low,mid,high):
            left = low
            right = mid + 1
            temp = []
            while left <= mid and right <= high:
                if nums[left] < nums[right]:
                    temp.append(nums[left])
                    left = left + 1
                else:
                    temp.append(nums[right])
                    right = right + 1
            while (left <= mid):
                temp.append(nums[left])
                left = left + 1
            while ( right <= high):
                temp.append(nums[right])
                right = right + 1
            for p3 in range(low,high+1):
                arr[p3] = temp[p3-low]
        divide(nums,0,len(nums)-1)
        return nums
            
            
