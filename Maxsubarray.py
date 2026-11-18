class Solution:
    def maxSubarraySum(self, arr, k):
        p1 = 0
        p2 = k-1
        sum1 = 0
        for x in range(p1,p2+1):
            sum1 += arr[x] 
        large = sum1
        while p2 < len(arr)-1:
            p1 += 1
            p2 += 1
            sum1 = sum1 + arr[p2] - arr[p1-1]
            if sum1 >= large:
                large = sum1
        return large
        
