class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns = list(s)
        nt = list(t)
        for i in ns:
            if i in nt:
                nt.remove(i)
            elif i not in nt:
                return False
        if len(nt) != 0:
            return False
        else:
            return True
        
