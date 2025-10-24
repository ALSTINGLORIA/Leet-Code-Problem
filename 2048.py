class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        newnum = n + 1
        val = 0
        while(True):
            num_list = list(str(newnum))
            for x in num_list:
                if num_list.count(x) == int(x):
                    val += 1
                else:
                    break
            if val == len(num_list):
                break
            val = 0
            newnum += 1
        return newnum
