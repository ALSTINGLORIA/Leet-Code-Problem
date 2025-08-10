class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = len(strs[0])
        count = 0
        pos = 0
        for i in strs:
            if mini > len(i):
                mini = len(i)
        
        for j in range(mini):
            alph = strs[0][j]
            count = 0
            for x in range(1,len(strs)):
                if strs[x][j] == alph:
                    count += 1  
            if count == (len(strs) -1):
                pos +=1
            else:
                break
        word = strs[0]
        words = word[0:pos]
        return words
