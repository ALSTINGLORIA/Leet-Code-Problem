class Solution:
    def hasSameDigits(self, s: str) -> bool:
        newString = ""
        while(len(s) > 2):
            for x in range(len(s)-1):
                newString += str((int(s[x]) + int(s[x+1])) % 10)
            s = newString
            newString = ""

        if s[0] != s[1]:
            return False
        else:
            return True
