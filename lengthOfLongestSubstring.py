class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        longest = 0
        large = 0
        while p2 < len(s):
            if s[p2] not in s[p1:p2]:
                p2 += 1
                large += 1
            elif s[p2] in s[p1:p2]:
                if large > longest:
                    longest = large
                large -= 1
                p1 += 1
        if large > longest:
            return large
        return longest
