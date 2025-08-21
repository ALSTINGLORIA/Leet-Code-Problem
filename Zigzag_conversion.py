class Solution:
    def convert(self, s: str, numRows: int) -> str:
        mid = abs(numRows-2)
        round = 0
        word = ""
        check = 0
        if numRows == 1:
            return s
        for x in range(1,numRows+1):
            point = x-1
            round = 0
            while point < len(s):
                round+=1
                if x !=1 and x!=numRows:
                    word += s[point]
                    if round%2!=0:
                        check = abs(numRows - x)
                        skip = (check*2)
                        point += skip
                    else:
                        check = abs(numRows - x)
                        skip = abs((numRows - check-1)*2)
                        point += skip
                else:
                    word += s[point]
                    point += (numRows+mid)
            
        return word
