class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for x in nums:
            var = max(x + rob1,rob2)
            rob1 = rob2
            rob2 = var

        return rob2
