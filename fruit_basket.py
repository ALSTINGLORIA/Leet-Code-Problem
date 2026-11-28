class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        p1 = 0
        p2 = 0
        large = 0 
        highest = 0
        allowed = {}
        while p2 < len(fruits):
            if fruits[p2] not in allowed and len(allowed) < 2:
                allowed[fruits[p2]] = 1
                p2 += 1
                large += 1
            elif fruits[p2] in allowed:
                allowed[fruits[p2]] += 1
                p2 += 1
                large += 1
            elif fruits[p2] not in allowed and len(allowed) >= 2:
                if allowed[fruits[p1]] == 1:
                    del allowed[fruits[p1]]
                else:
                    allowed[fruits[p1]] -= 1
                p1 += 1
                large -= 1
            if large > highest:
                    highest = large
                
        return highest
