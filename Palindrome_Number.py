class Solution:
    def isPalindrome(self, x: int) -> bool:
        og_num = x
        new_num = 0
        mul = 10
        if( x < 0):
            return False
        while x != 0:
            new_num = new_num * mul
            new_num = new_num + (x % 10)
            x = x // 10
        
        if(new_num == og_num):
            final = True
        elif( new_num != og_num):
            final = False

        return final
