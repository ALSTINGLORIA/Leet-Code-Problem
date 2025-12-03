class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        p1 = p2 = float('inf')

        for x  in nums:
            if(x <= p1):
                p1 = x
            elif(x <= p2):
                p2 = x
            else:
                return True
        return False
        
                
        


            
        
