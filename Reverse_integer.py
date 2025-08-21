class Solution:
    def reverse(self, x: int) -> int:
        minus = 0
        if x >= 0:
            string = str(x)
        else:
            string = str(abs(x))
            minus = 1
        string = string.lstrip('0')
        string = string[::-1]
        if minus == 1 and len(string)!=0:
            string = "-" + string
        elif len(string) == 0:
            string="0"
        num = int(string)
        if num > -2**31 and num < 2**31:
            return num
        else:
            return 0
