class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = 1
        store = ""
        stack = ""
        while left < len(s):
            store = ""
            for i in range(left,len(s)):
                store += s[i]
                if store == store[::-1] and len(stack) < len(store):
                    stack = store
            left+=1
        return stack





