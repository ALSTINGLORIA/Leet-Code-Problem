class Solution:
    def bubbleSort(self, nums):
        def sort(arr,curr,pos):
            if curr < len(arr):
                if pos < len(arr)-curr:
                    if arr[pos] < arr[pos-1]:
                        arr[pos],arr[pos-1] = arr[pos-1],arr[pos]
                    pos = pos + 1
                else:
                    pos = 1
                    curr = curr + 1
                sort(arr,curr,pos)
            return arr
        
        return sort(nums,0,1)
                


