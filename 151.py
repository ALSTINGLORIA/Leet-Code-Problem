class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        count = 0
        ns = []
        old = ""
        string = ""
        for x in s:
            if x == " " and count==0:
                ns.append(old)
                ns.append(" ")
                old = ""
                count+=1
            elif x == " " and count==1:
                continue
            elif x != " ":
                count = 0
                old += x
        ns.append(old)
        for x in ns[::-1]:
            string += x
        return string
