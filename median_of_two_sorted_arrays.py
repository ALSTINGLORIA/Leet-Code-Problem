class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        for x in nums1:
            nums3.append(x)
        for y in nums2:
            nums3.append(y)
        num = 0
        nums3 = sorted(nums3)
        if len(nums3) == 1:
            return nums3[0]
        elif(len(nums3)%2)!=0:
            num = nums3[len(nums3) // 2]
            return num
        else:
            num = (nums3[(len(nums3)//2)-1] + nums3[((len(nums3)//2))])/2
            return num
