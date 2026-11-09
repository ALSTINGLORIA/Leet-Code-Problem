class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        p1 = 0
        p2 = 1
        p3 = len(arr)-1
        ans = 0
        while p1 < len(arr)-2:
            while p2 < p3:
                sum1 = arr[p1] + arr[p2] + arr[p3]
                if sum1 < sum:
                    ans = ans + (p3 - p2)
                    p2 += 1
                elif sum1 >= sum:
                    p3 -= 1
            p1 += 1
            p2 = p1 + 1
            p3 = len(arr)-1
        return ans
            
            
        
        
