class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = s.lower()
        st = ""
        for alp in ns:
            if alp.isalnum():
                st += alp
        if st[::-1] != st[0:len(st)]:
            return False
        else:
            return True
