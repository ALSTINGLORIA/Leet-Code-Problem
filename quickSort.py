class Solution:
    def quickSort(self, nums):
        def partitionDivide(arr,low,high):
            if low < high:
                partition = partitionFinder(arr,low,high)
                partitionDivide(arr,low,partition-1)
                partitionDivide(arr,partition+1,high)


        def partitionFinder(arr,low,high):
            left,right = low+1,high
            while left < right:
                while left <= high-1 and arr[left] <= arr[low]:
                    left = left + 1

                while right >= low+1 and arr[right] > arr[low]:
                    right = right - 1

                if left < right:
                    arr[left],arr[right] = arr[right],arr[left]
                    

            arr[right],arr[low] = arr[low],arr[right]
            return right

        partitionDivide(nums,0,len(nums)-1)
        return nums
        



     
