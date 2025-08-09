class Solution:
    def isValid(self, s: str) -> bool:
        sta = []
        top = -1
        count1 = 0
        count2 = 0
        count = 0
        for i in s:
            count +=1
            if i == '(' or i == '{' or i == '[':
                sta.append(i)
                top +=1
                count2 +=1
            elif sta:
                if ((i == ')' and sta[top] == '(') or (i == '}' and sta[top] == '{') or (i == ']' and sta[top] == '[')):
                    sta.pop()
                    top -= 1
                    count1 +=1
        if (count1 == count2) and (count1 + count2 == count):
            return True
        else:
            return False

