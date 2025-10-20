class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        for x in operations:
            if x == "X++" or x == "++X":
                val += 1
            else:
                val -= 1
        return val
