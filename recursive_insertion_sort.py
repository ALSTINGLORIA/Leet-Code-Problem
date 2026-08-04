class Solution:
    def insertionSort(self, nums):
        def sort(arr,right,curr):
            if right <= len(arr)-1:
                if curr > 0:
                    if arr[curr] < arr[curr-1]:
                        arr[curr],arr[curr-1] = arr[curr-1],arr[curr]
                        curr = curr - 1
                        sort(arr,right,curr)
                    else:
                        sort(arr,right+1,right+1)
                else:
                    sort(arr,right+1,right+1)
            return arr

        return sort(nums,0,0)

            


