class Solution:
    def totalMoney(self, n: int) -> int:
        sum1 = 0
        day = 0
        count = 1
        val = 0
        nval = 1
        while(count <= n):
            if day == 7:
                nval += 1
                sum1 += nval
                day = 1
                val = nval
            else:
                val += 1
                sum1 += val
                day += 1
                
            count += 1
        return sum1
