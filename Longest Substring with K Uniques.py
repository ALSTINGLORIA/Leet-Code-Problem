class Solution:
    def longestKSubstr(self, s, k):
        p1 =0
        p2 =0 
        count = 0
        size =1
        maxval = -1
        hashmap = {}
        while p2 <len(s):
            if s[p2] in hashmap:
                hashmap[s[p2]] += 1
                p2 += 1
                size += 1
            elif count < k:
                hashmap[s[p2]] = 1
                p2 += 1
                count += 1
                size += 1
            else:
                hashmap[s[p1]] -= 1
                if hashmap[s[p1]] == 0:
                    del hashmap[s[p1]]
                    count -=1
                p1 += 1
                size -= 1
            if size > maxval and count ==k:
                    maxval = size -1
        return maxval
            
                
            
        
        
