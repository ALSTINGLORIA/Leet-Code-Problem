class Solution:
    def myAtoi(self, s: str) -> int:
        ns = s.strip()
        final = ""
        sign = ""
        if ns == "":
            return 0
        if ns[0] == "+":
            sign = "+" 
        elif ns[0] == "-":
            sign = "-" 
        if sign == "":
            for x in ns:
                if x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9":
                    final += x
                else:
                    break
        else:
            for x in ns[1:]:
                if x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9":
                    final += x
                else:
                    break
        if final.isdigit():
            final = sign + final
            if ((2**31)-1) >= int(final) >= (-2**31):
                return int(final)
            elif ((2**31)-1) < int(final):
                return ((2**31)-1)
            elif int(final) < (-2**31):
                return (-2**31)
        else:
            return 0
